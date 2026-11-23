# TaskManager-DevOps

Sistema web para la gestión de tareas.

Proyecto desarrollado para la empresa ficticia **TechSolutions**, que necesita
reemplazar sus hojas de cálculo por una aplicación web centralizada para
registrar, consultar, editar, eliminar, cambiar el estado y priorizar tareas.

Este repositorio implementa, además del sistema, las fases del ciclo de vida
**DevOps** (Plan, Code, Build/CI, Test, Release, Deploy, Operate & Monitor)
utilizando GitHub como plataforma principal.

## Funcionalidades (requerimientos funcionales)

| Código | Funcionalidad     | Descripción                                   |
| ------ | ----------------- | ---------------------------------------------- |
| RF01   | Registrar tareas  | Permitir agregar nuevas tareas.                |
| RF02   | Consultar tareas  | Mostrar todas las tareas registradas.          |
| RF03   | Editar tareas     | Modificar la información de una tarea.         |
| RF04   | Eliminar tareas   | Eliminar tareas existentes.                    |
| RF05   | Cambiar estado    | Cambiar entre pendiente, en proceso y terminada. |
| RF06   | Asignar prioridad | Clasificar tareas como alta, media o baja.     |

## Tecnologías

- **Frontend:** HTML, CSS y JavaScript (vanilla).
- **Backend:** Python con Flask.
- **Base de datos:** SQLite.
- **Control de versiones:** Git / GitHub.
- **Automatización:** GitHub Actions.
- **Pruebas:** Pytest.
- **Despliegue:** Render / Railway / Fly.io (compatible con Flask + gunicorn).

## Estructura del proyecto

```
TaskManager-DevOps/
│
├── app.py
├── requirements.txt
├── README.md
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/style.css
│   └── js/app.js
│
├── tests/
│   └── test_app.py
│
├── docs/
│   ├── historias_usuario.md
│   ├── issues.md
│   ├── casos_prueba.md
│   └── monitoreo.md
│
└── .github/workflows/
    ├── ci.yml
    └── cd.yml
```

## Ejecutar en local

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
```

La aplicación queda disponible en `http://127.0.0.1:5000`.

## Ejecutar las pruebas

```bash
pip install -r requirements.txt
pytest
```

## Flujo de ramas utilizado

- `main`: versión estable del proyecto.
- `feature/registro-tareas`: RF01 y RF02 (registrar/consultar).
- `feature/editar-tareas`: RF03, RF05 y RF06 (editar, estado, prioridad).
- `feature/eliminar-tareas`: RF04 (eliminar).

Cada rama se integró a `main` mediante un Pull Request revisado antes de
combinarse (ver pestaña **Pull requests** del repositorio).

## Integración continua y despliegue

- `.github/workflows/ci.yml` ejecuta `pytest` automáticamente en cada `push`
  y `pull_request` hacia `main`.
- `.github/workflows/cd.yml` genera un artefacto descargable del proyecto
  cada vez que se publica un *release* en GitHub.
- El despliegue en vivo corre con `gunicorn app:app` sobre la plataforma
  cloud seleccionada (ver sección de despliegue en el documento de
  resultados).
