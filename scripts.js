// Obtener el enlace de "Servicios" por su ID
var serviciosLink = document.getElementById("servicios-link");
var hogarLink = document.getElementById("hogar-link");
// Agregar un evento de clic al enlace de "Servicios"
serviciosLink.addEventListener("click", function(event) {
    // Prevenir el comportamiento predeterminado del enlace
    event.preventDefault();
    
    // Redirigir a la página deseada (por ejemplo, "pagina2.html")
    window.location.href = "servicios.html";
});

// Agregar un evento de clic al enlace de "Hogar"

hogarLink.addEventListener("click", function(event) {
    // Prevenir el comportamiento predeterminado del enlace
    event.preventDefault();
    
    // Redirigir a la página deseada (por ejemplo, "pagina2.html")
    window.location.href = "home.html";
});
