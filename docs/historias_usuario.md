# Historias de usuario — TaskManager

> Fase 1 (Plan) · Actividad 3. Estas historias se usaron también como base
> para las Issues y el tablero de GitHub Projects.

## Historia de usuario 1: Registrar tareas

Como usuario del sistema, quiero registrar nuevas tareas para organizar mis
actividades.

**Criterios de aceptación**
- El sistema debe permitir ingresar el nombre de la tarea.
- El sistema debe permitir agregar una descripción.
- El sistema debe permitir seleccionar una prioridad.
- El sistema debe guardar la tarea.
- El sistema debe mostrar un mensaje de confirmación o el error si falta el
  nombre.

## Historia de usuario 2: Cambiar estado de tareas

Como usuario, quiero cambiar el estado de una tarea para conocer su
progreso.

**Criterios de aceptación**
- Debe permitir seleccionar pendiente.
- Debe permitir seleccionar en proceso.
- Debe permitir seleccionar terminada.
- El cambio debe reflejarse en el listado de tareas.

## Historia de usuario 3: Consultar tareas

Como usuario, quiero ver el listado completo de tareas registradas para
saber qué actividades existen.

**Criterios de aceptación**
- El sistema debe mostrar nombre, descripción, prioridad y estado de cada
  tarea.
- El listado debe actualizarse al crear, editar o eliminar una tarea.
- Si no hay tareas, debe mostrarse un mensaje indicándolo.

## Historia de usuario 4: Editar tareas

Como usuario, quiero modificar una tarea existente para corregir o
actualizar su información.

**Criterios de aceptación**
- Debe permitir cambiar nombre, descripción y prioridad.
- El sistema debe validar que el nombre no quede vacío.
- Los cambios deben reflejarse de inmediato en el listado.

## Historia de usuario 5: Eliminar tareas

Como usuario, quiero eliminar una tarea que ya no es necesaria para mantener
organizado el listado.

**Criterios de aceptación**
- El sistema debe solicitar confirmación antes de eliminar.
- La tarea eliminada debe desaparecer del listado.
- No debe ser posible eliminar una tarea que no existe (error controlado).

## Historia de usuario 6: Asignar prioridad

Como usuario, quiero clasificar cada tarea como alta, media o baja
prioridad para decidir en qué orden atenderlas.

**Criterios de aceptación**
- La prioridad debe asignarse al crear la tarea (por defecto "Media").
- La prioridad debe poder modificarse al editar la tarea.
- El sistema debe rechazar valores de prioridad distintos a
  Alta/Media/Baja.
