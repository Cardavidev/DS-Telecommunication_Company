//ID
var serviciosLink = document.getElementById("servicios-link");
var hogarLink = document.getElementById("hogar-link");
var inicio_sesionlink=document.getElementById("inicio-sesion-link");
var registro_usuariolink = document.getElementById("registro_usuario");

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

// Agregar un evento de clic al enlace de "Inicio de sesión"
inicio_sesionlink.addEventListener("click", function(event) {
    // Prevenir el comportamiento predeterminado del enlace
    event.preventDefault();
    
    // Redirigir a la página deseada (por ejemplo, "pagina2.html")
    window.location.href = "inicio_sesion.html";
});

// Agregar un evento de clic al enlace de "Registro_usuario"
registro_usuariolink.addEventListener("click", function(event) {
    // Prevenir el comportamiento predeterminado del enlace
    event.preventDefault();
    
    // Redirigir a la página deseada (por ejemplo, "pagina2.html")
    window.location.href = "registro_usuario.html";
});