# Issues registrados — TaskManager

> Fase 1 (Plan) · Actividad 4. Cada fila se crea como un Issue en GitHub
> (pestaña **Issues**) y se agrega al tablero de **GitHub Projects**, con
> las propiedades: Responsable (Assignees), Estado (Status), Prioridad
> (Single select), Estimación (Number, horas) y Fase DevOps (Single
> select).

| # | Título | Fase DevOps | Prioridad | Estimación (h) | Estado inicial |
|---|--------|-------------|-----------|-----------------|-----------------|
| 1 | Crear la estructura inicial del proyecto | Plan | Alta | 2 | Done |
| 2 | Diseñar la interfaz del sistema | Code | Media | 3 | Done |
| 3 | Implementar el registro de tareas (RF01) | Code | Alta | 4 | Done |
| 4 | Implementar la consulta de tareas (RF02) | Code | Alta | 2 | Done |
| 5 | Implementar la edición de tareas (RF03) | Code | Media | 3 | Done |
| 6 | Implementar la eliminación de tareas (RF04) | Code | Media | 2 | Done |
| 7 | Implementar el cambio de estado (RF05) | Code | Media | 2 | Done |
| 8 | Implementar la asignación de prioridad (RF06) | Code | Media | 2 | Done |
| 9 | Implementar las pruebas unitarias | Test | Alta | 4 | Done |
| 10 | Configurar GitHub Actions (CI) | Build | Alta | 3 | Done |
| 11 | Configurar GitHub Actions (CD) y Release v1.0.0 | Release | Media | 2 | Done |
| 12 | Configurar despliegue en la nube | Deploy | Alta | 3 | Pendiente |
| 13 | Configurar monitoreo y registro de incidencias | Operate | Media | 2 | Pendiente |

## Comandos sugeridos para crearlos con GitHub CLI

Una vez autenticado (`gh auth login`) y con el repositorio ya creado y
clonado:

```bash
gh issue create --title "Crear la estructura inicial del proyecto" \
  --body "Fase: Plan. Crear carpetas app.py, templates/, static/, tests/." \
  --label "plan"

gh issue create --title "Implementar el registro de tareas (RF01)" \
  --body "Fase: Code. Endpoint POST /api/tareas y formulario en index.html." \
  --label "code"
```

(Repetir con el resto de títulos de la tabla; asignar prioridad/estimación
desde el tablero de Projects, ya que esos campos personalizados no se
pueden fijar por `gh issue create`.)

## Ejemplo de Issue de error (Fase 4 — Pruebas)

**Título:** Error al guardar tareas sin descripción.

**Descripción:**
- Funcionalidad afectada: Registro de tareas.
- Pasos para reproducir: Intentar guardar una tarea sin descripción.
- Resultado obtenido: (completar tras la prueba manual)
- Resultado esperado: El sistema debe aceptar la tarea, ya que la
  descripción es opcional según RF01; solo el nombre es obligatorio.
- Prioridad: Alta.
