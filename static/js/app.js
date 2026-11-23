const formulario = document.getElementById("form-tarea");
const campoNombre = document.getElementById("nombre");
const campoDescripcion = document.getElementById("descripcion");
const campoPrioridad = document.getElementById("prioridad");
const mensajeError = document.getElementById("mensaje-error");
const cuerpoTabla = document.getElementById("cuerpo-tabla");
const mensajeVacio = document.getElementById("mensaje-vacio");

async function obtenerTareas() {
  const respuesta = await fetch("/api/tareas");
  const tareas = await respuesta.json();
  renderizarTareas(tareas);
}

function badgePrioridad(prioridad) {
  const clase =
    prioridad === "Alta" ? "badge-alta" : prioridad === "Baja" ? "badge-baja" : "badge-media";
  return `<span class="badge ${clase}">${prioridad}</span>`;
}

function escaparHtml(texto) {
  const div = document.createElement("div");
  div.textContent = texto;
  return div.innerHTML;
}

function renderizarTareas(tareas) {
  cuerpoTabla.innerHTML = "";
  mensajeVacio.hidden = tareas.length !== 0;

  for (const tarea of tareas) {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${escaparHtml(tarea.nombre)}</td>
      <td>${escaparHtml(tarea.descripcion || "")}</td>
      <td>${badgePrioridad(tarea.prioridad)}</td>
      <td>${escaparHtml(tarea.estado)}</td>
    `;
    cuerpoTabla.appendChild(fila);
  }
}

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  mensajeError.hidden = true;

  const cuerpo = {
    nombre: campoNombre.value.trim(),
    descripcion: campoDescripcion.value.trim(),
    prioridad: campoPrioridad.value,
  };

  const respuesta = await fetch("/api/tareas", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(cuerpo),
  });

  if (!respuesta.ok) {
    const datos = await respuesta.json().catch(() => ({}));
    mensajeError.textContent = datos.error || "Ocurrió un error al guardar la tarea.";
    mensajeError.hidden = false;
    return;
  }

  formulario.reset();
  campoPrioridad.value = "Media";
  await obtenerTareas();
});

obtenerTareas();
