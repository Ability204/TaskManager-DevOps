import os
import sqlite3

from flask import Flask, g, jsonify, render_template, request

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tareas.db")

ESTADOS_VALIDOS = {"Pendiente", "En proceso", "Terminada"}
PRIORIDADES_VALIDAS = {"Alta", "Media", "Baja"}


def get_db_connection(database_path):
    conexion = sqlite3.connect(database_path)
    conexion.row_factory = sqlite3.Row
    return conexion


def init_db(database_path):
    conexion = get_db_connection(database_path)
    conexion.execute(
        """
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL DEFAULT '',
            prioridad TEXT NOT NULL DEFAULT 'Media',
            estado TEXT NOT NULL DEFAULT 'Pendiente'
        )
        """
    )
    conexion.commit()
    conexion.close()


def create_app(database_path=DATABASE):
    app = Flask(__name__)
    app.config["DATABASE"] = database_path
    init_db(database_path)

    def db():
        if "db" not in g:
            g.db = get_db_connection(app.config["DATABASE"])
        return g.db

    @app.teardown_appcontext
    def cerrar_db(exception=None):
        conexion = g.pop("db", None)
        if conexion is not None:
            conexion.close()

    @app.route("/")
    def index():
        return render_template("index.html")

    # RF02 - Consultar tareas: mostrar todas las tareas registradas.
    @app.route("/api/tareas", methods=["GET"])
    def listar_tareas():
        filas = db().execute("SELECT * FROM tareas ORDER BY id DESC").fetchall()
        return jsonify([dict(fila) for fila in filas])

    # RF01 - Registrar tareas: permitir agregar nuevas tareas.
    @app.route("/api/tareas", methods=["POST"])
    def crear_tarea():
        datos = request.get_json(silent=True) or {}
        nombre = (datos.get("nombre") or "").strip()
        if not nombre:
            return jsonify({"error": "El nombre de la tarea es obligatorio."}), 400

        prioridad = datos.get("prioridad") or "Media"
        if prioridad not in PRIORIDADES_VALIDAS:
            return jsonify({"error": "Prioridad inválida."}), 400

        descripcion = (datos.get("descripcion") or "").strip()

        cursor = db().execute(
            "INSERT INTO tareas (nombre, descripcion, prioridad, estado) VALUES (?, ?, ?, 'Pendiente')",
            (nombre, descripcion, prioridad),
        )
        db().commit()
        fila = db().execute("SELECT * FROM tareas WHERE id = ?", (cursor.lastrowid,)).fetchone()
        return jsonify(dict(fila)), 201

    # RF03 - Editar tareas: modificar la información de una tarea.
    @app.route("/api/tareas/<int:tarea_id>", methods=["PUT"])
    def editar_tarea(tarea_id):
        fila = db().execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
        if fila is None:
            return jsonify({"error": "Tarea no encontrada."}), 404

        datos = request.get_json(silent=True) or {}
        nombre = (datos.get("nombre", fila["nombre"]) or "").strip()
        if not nombre:
            return jsonify({"error": "El nombre de la tarea es obligatorio."}), 400

        prioridad = datos.get("prioridad", fila["prioridad"])
        if prioridad not in PRIORIDADES_VALIDAS:
            return jsonify({"error": "Prioridad inválida."}), 400

        descripcion = datos.get("descripcion", fila["descripcion"])

        db().execute(
            "UPDATE tareas SET nombre = ?, descripcion = ?, prioridad = ? WHERE id = ?",
            (nombre, descripcion, prioridad, tarea_id),
        )
        db().commit()
        fila = db().execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
        return jsonify(dict(fila))

    # RF05 - Cambiar estado: cambiar entre pendiente, en proceso y terminada.
    @app.route("/api/tareas/<int:tarea_id>/estado", methods=["PATCH"])
    def cambiar_estado(tarea_id):
        fila = db().execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
        if fila is None:
            return jsonify({"error": "Tarea no encontrada."}), 404

        datos = request.get_json(silent=True) or {}
        estado = datos.get("estado")
        if estado not in ESTADOS_VALIDOS:
            return jsonify({"error": "Estado inválido."}), 400

        db().execute("UPDATE tareas SET estado = ? WHERE id = ?", (estado, tarea_id))
        db().commit()
        fila = db().execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
        return jsonify(dict(fila))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
