# Matriz de casos de prueba — TaskManager

> Fase 4 (Test) · Actividad 1 y 2.

| ID | Prueba | Resultado esperado | Resultado obtenido |
|----|--------|---------------------|----------------------|
| CP01 | Registrar una tarea | La tarea se guarda correctamente. | OK — `test_registro_tarea` y prueba manual en navegador. |
| CP02 | Registrar una tarea sin nombre | El sistema muestra una validación. | OK — `test_registro_tarea_sin_nombre` (HTTP 400) y mensaje en el formulario. |
| CP03 | Consultar tareas | Se muestra el listado. | OK — `test_consultar_tareas`. |
| CP04 | Editar una tarea | Se actualiza la información. | OK — `test_editar_tarea`. |
| CP05 | Eliminar una tarea | La tarea desaparece del listado. | OK — `test_eliminar_tarea`. |
| CP06 | Cambiar estado | Se actualiza el estado. | OK — `test_cambiar_estado` (y rechazo de estados inválidos, `test_cambiar_estado_invalido`). |
| CP07 | Seleccionar prioridad | Se guarda la prioridad elegida. | OK — `test_asignar_prioridad`. |

## Prueba funcional manual — CP01 (ejemplo del documento)

1. Abrir el sistema (`http://127.0.0.1:5000` en local, o la URL pública).
2. En el formulario "Nueva tarea", escribir el nombre:
   `Elaborar documentación`.
3. Agregar una descripción.
4. Seleccionar prioridad **Alta**.
5. Hacer clic en **Guardar tarea**.
6. Verificar que la tarea aparezca en el listado con prioridad Alta y
   estado Pendiente.

**Resultado esperado:** la tarea debe registrarse correctamente.
