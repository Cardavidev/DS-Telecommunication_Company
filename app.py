from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

# Diccionario para almacenar los datos de los usuarios
usuarios = {}

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/registro_usuario')
def registrar_usuario():
    return render_template('registro_usuario.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    # Obtén los datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    cedula = request.form.get('cedula')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')

    # Verifica si el usuario ya existe en el diccionario
    if cedula in usuarios:
        return render_template('registro_usuario.html', error="El usuario ya existe.")

    # Almacena los datos del usuario en el diccionario
    usuarios[cedula] = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
        'contraseña': contraseña
    }

    return render_template('inicio_sesion.html')

# Ruta de inicio de sesión
@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    cedula = request.form.get('cedula')
    contraseña = request.form.get('contraseña')

    # Verifica si el usuario existe en el diccionario y si la contraseña coincide
    if cedula in usuarios and usuarios[cedula]['contraseña'] == contraseña:
        return render_template('home.html')

    # Si las credenciales no coinciden, muestra un mensaje de error
    return render_template('inicio_sesion.html', error="Credenciales incorrectas")

if __name__ == '__main__':
    app.run(debug=True)
