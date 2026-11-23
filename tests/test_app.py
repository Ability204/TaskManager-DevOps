import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from app import create_app


@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test_tareas.db"
    app = create_app(database_path=str(db_path))
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


def test_registro_tarea(client):
    respuesta = client.post(
        "/api/tareas",
        json={
            "nombre": "Realizar actividad DevOps",
            "descripcion": "Completar el remedial",
            "prioridad": "Alta",
        },
    )
    assert respuesta.status_code == 201
    datos = respuesta.get_json()
    assert datos["nombre"] == "Realizar actividad DevOps"
    assert datos["estado"] == "Pendiente"
    assert datos["prioridad"] == "Alta"


def test_registro_tarea_sin_nombre(client):
    respuesta = client.post("/api/tareas", json={"descripcion": "sin nombre"})
    assert respuesta.status_code == 400


def test_consultar_tareas(client):
    client.post("/api/tareas", json={"nombre": "Tarea 1"})
    client.post("/api/tareas", json={"nombre": "Tarea 2"})
    respuesta = client.get("/api/tareas")
    datos = respuesta.get_json()
    assert len(datos) == 2


def test_editar_tarea(client):
    creada = client.post("/api/tareas", json={"nombre": "Original"}).get_json()
    respuesta = client.put(f"/api/tareas/{creada['id']}", json={"nombre": "Editada"})
    assert respuesta.status_code == 200
    assert respuesta.get_json()["nombre"] == "Editada"


def test_editar_tarea_inexistente(client):
    respuesta = client.put("/api/tareas/999", json={"nombre": "No existe"})
    assert respuesta.status_code == 404


def test_eliminar_tarea(client):
    creada = client.post("/api/tareas", json={"nombre": "Para borrar"}).get_json()
    respuesta = client.delete(f"/api/tareas/{creada['id']}")
    assert respuesta.status_code == 200
    restante = client.get("/api/tareas").get_json()
    assert restante == []


def test_cambiar_estado(client):
    creada = client.post("/api/tareas", json={"nombre": "Tarea"}).get_json()
    respuesta = client.patch(
        f"/api/tareas/{creada['id']}/estado", json={"estado": "En proceso"}
    )
    assert respuesta.status_code == 200
    assert respuesta.get_json()["estado"] == "En proceso"


def test_cambiar_estado_invalido(client):
    creada = client.post("/api/tareas", json={"nombre": "Tarea"}).get_json()
    respuesta = client.patch(
        f"/api/tareas/{creada['id']}/estado", json={"estado": "Cancelada"}
    )
    assert respuesta.status_code == 400


def test_asignar_prioridad(client):
    creada = client.post(
        "/api/tareas", json={"nombre": "Tarea", "prioridad": "Baja"}
    ).get_json()
    assert creada["prioridad"] == "Baja"

    editada = client.put(
        f"/api/tareas/{creada['id']}", json={"prioridad": "Alta"}
    ).get_json()
    assert editada["prioridad"] == "Alta"
