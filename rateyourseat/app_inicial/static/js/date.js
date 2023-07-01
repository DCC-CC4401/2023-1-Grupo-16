const fechaInput = document.getElementById("fecha");
const fechaActual = new Date().toISOString().split("T")[0];
fechaInput.setAttribute("max", fechaActual);


document.addEventListener("DOMContentLoaded", function() {
    var porFechaOption = document.getElementById("porFecha");
    var fechaInput = document.getElementById("fecha");

    porFechaOption.addEventListener("click", function() {
      fechaInput.style.display = fechaInput.style.display === "none" ? "block" : "none";
    });
  });