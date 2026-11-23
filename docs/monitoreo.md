# Operación y monitoreo — TaskManager

> Fase 7 (Operate & Monitor).

## Actividad 1. Monitoreo del funcionamiento

- **Disponibilidad de la aplicación:** verificar periódicamente que la URL
  pública responda (por ejemplo con el *health check* del propio servicio
  de despliegue).
- **Tiempo de respuesta:** observado en las herramientas de métricas del
  proveedor (Render/Railway/Fly.io) tras el despliegue.
- **Errores del sistema:** revisar los logs del servicio de despliegue.
- **Almacenamiento de información:** confirmar que las tareas persistan en
  `tareas.db` entre reinicios del servicio (en planes gratuitos el disco
  puede no ser persistente; ver nota en el documento de resultados).
- **Funcionalidades principales:** repetir manualmente CP01–CP07 sobre la
  URL pública.

## Actividad 2. Registro de incidencias (ejemplo)

**Título:** La aplicación no permite guardar nuevas tareas.

- **Fecha de detección:** (completar al desplegar)
- **Funcionalidad afectada:** Registro de tareas (RF01).
- **Descripción del problema:** (completar si ocurre)
- **Evidencia del error:** captura de pantalla / mensaje de la consola.
- **Responsable de corregirlo:** Luis Joel Gómez Herrera.
- **Solución aplicada:** (completar)

## Actividad 3. Mejoras propuestas para una futura versión

1. Implementar autenticación de usuarios (login por integrante del
   equipo), para saber quién creó o modificó cada tarea.
2. Agregar filtros y búsqueda por nombre, estado o prioridad en el
   listado.
3. Incorporar notificaciones (por ejemplo, correo o recordatorio) cuando
   una tarea de prioridad alta lleve mucho tiempo en estado "Pendiente".
4. Agregar reportes de productividad (tareas completadas por semana).
5. Mejorar el rendimiento migrando de SQLite a una base de datos cliente-
   servidor (PostgreSQL) si el número de tareas crece mucho.
