const formulario = document.getElementById("form-tarea");
const campoId = document.getElementById("tarea-id");
const campoNombre = document.getElementById("nombre");
const campoDescripcion = document.getElementById("descripcion");
const campoPrioridad = document.getElementById("prioridad");
const botonCancelar = document.getElementById("btn-cancelar");
const formTitulo = document.getElementById("form-titulo");
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
      <td>
        <select class="estado-select" data-id="${tarea.id}">
          <option value="Pendiente" ${tarea.estado === "Pendiente" ? "selected" : ""}>Pendiente</option>
          <option value="En proceso" ${tarea.estado === "En proceso" ? "selected" : ""}>En proceso</option>
          <option value="Terminada" ${tarea.estado === "Terminada" ? "selected" : ""}>Terminada</option>
        </select>
      </td>
      <td class="fila-acciones">
        <button type="button" class="secundario btn-editar" data-id="${tarea.id}">Editar</button>
        <button type="button" class="peligro btn-eliminar" data-id="${tarea.id}">Eliminar</button>
      </td>
    `;
    cuerpoTabla.appendChild(fila);
  }
}

function limpiarFormulario() {
  campoId.value = "";
  formulario.reset();
  campoPrioridad.value = "Media";
  formTitulo.textContent = "Nueva tarea";
  botonCancelar.hidden = true;
  mensajeError.hidden = true;
}

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  mensajeError.hidden = true;

  const cuerpo = {
    nombre: campoNombre.value.trim(),
    descripcion: campoDescripcion.value.trim(),
    prioridad: campoPrioridad.value,
  };

  const id = campoId.value;
  const url = id ? `/api/tareas/${id}` : "/api/tareas";
  const metodo = id ? "PUT" : "POST";

  const respuesta = await fetch(url, {
    method: metodo,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(cuerpo),
  });

  if (!respuesta.ok) {
    const datos = await respuesta.json().catch(() => ({}));
    mensajeError.textContent = datos.error || "Ocurrió un error al guardar la tarea.";
    mensajeError.hidden = false;
    return;
  }

  limpiarFormulario();
  await obtenerTareas();
});

botonCancelar.addEventListener("click", () => {
  limpiarFormulario();
});

cuerpoTabla.addEventListener("click", async (evento) => {
  const boton = evento.target.closest("button");
  if (!boton) return;
  const id = boton.dataset.id;

  if (boton.classList.contains("btn-eliminar")) {
    const confirmado = confirm("¿Eliminar esta tarea?");
    if (!confirmado) return;
    await fetch(`/api/tareas/${id}`, { method: "DELETE" });
    await obtenerTareas();
    return;
  }

  if (boton.classList.contains("btn-editar")) {
    const respuesta = await fetch("/api/tareas");
    const tareas = await respuesta.json();
    const tarea = tareas.find((t) => String(t.id) === String(id));
    if (!tarea) return;

    campoId.value = tarea.id;
    campoNombre.value = tarea.nombre;
    campoDescripcion.value = tarea.descripcion;
    campoPrioridad.value = tarea.prioridad;
    formTitulo.textContent = `Editar tarea #${tarea.id}`;
    botonCancelar.hidden = false;
  }
});

cuerpoTabla.addEventListener("change", async (evento) => {
  const select = evento.target.closest(".estado-select");
  if (!select) return;

  await fetch(`/api/tareas/${select.dataset.id}/estado`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ estado: select.value }),
  });

  await obtenerTareas();
});

obtenerTareas();
