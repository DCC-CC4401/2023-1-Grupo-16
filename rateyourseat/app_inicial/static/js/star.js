// Obtén el contenedor de las estrellas
var starsContainer = document.getElementById('stars-container');
const stars_container = document.querySelector("#stars-container")

// Define el valor numérico de las estrellas (1-5)
var valorEstrellas = parseInt(starsContainer.dataset.stars);

// Genera las etiquetas <label> y aplica las clases correspondientes
for (var i = 1; i <= 5; i++) {
  var starLabel = document.createElement('label');
  
  starLabel.classList.add('star');
  
  if (i <= valorEstrellas) {
    starLabel.classList.add('star-filled');
  }
  
  starLabel.textContent = '\u2605'; // Agrega el carácter Unicode para la estrella
  
  starsContainer.appendChild(starLabel);
}