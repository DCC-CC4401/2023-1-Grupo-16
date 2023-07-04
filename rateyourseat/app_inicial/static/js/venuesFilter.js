const sit={
    "recintos": [
      {"nombre": "Movistar Arena"},
      {"nombre": "Teatro Cariola"},
      {"nombre": "Teatro Caupolicán"},
      {"nombre": "Estadio Nacional"},
      {"nombre": "Club Hípico"},
      {"nombre": "Estadio Monumental"},
      {"nombre": "Estadio Bicentenario de la Florida"},
      {"nombre": "Casa CEI"},
    ]
}

const recintoSelect = document.getElementById("venueFilter");

// Llenar el select de recintos con las opciones del JSON
sit.recintos.forEach(recinto => {
    const option = document.createElement("option");
    option.value = recinto.nombre;
    option.textContent = recinto.nombre;
    recintoSelect.appendChild(option);
}); 

