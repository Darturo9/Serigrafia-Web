"use strict";
const principal = document.getElementById("foto-principal");
const estado = document.getElementById("estado-foto");
const miniaturas = [...document.querySelectorAll(".miniatura-producto")];
for (const enlace of miniaturas) {
  enlace.addEventListener("click", (evento) => {
    if (evento.ctrlKey || evento.metaKey || evento.shiftKey || evento.altKey) return;
    evento.preventDefault();
    principal.src = enlace.dataset.foto;
    principal.alt = enlace.dataset.descripcion;
    for (const otra of miniaturas) otra.removeAttribute("aria-current");
    enlace.setAttribute("aria-current", "true");
    estado.textContent = `Foto ${enlace.dataset.numero} de ${miniaturas.length}`;
  });
}
if (principal) principal.addEventListener("error", () => {
  estado.textContent = "No se pudo cargar esta foto. Prueba otra imagen o vuelve a cargar la página.";
});
