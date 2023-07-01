var select = document.getElementById('fecha-select');
var inputFecha = document.getElementById('fecha');


select.addEventListener("click", function() {
    var options = activities.querySelectorAll("option");
    //unhide
});

select.addEventListener("change", function() {
    if(select.value == 'Por fecha'){
      inputFecha.style.display = 'block';
    }
    else{
      inputFecha.style.display = 'none';
    }
});