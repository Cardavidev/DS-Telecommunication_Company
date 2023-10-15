from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__, static_folder='static')
app.secret_key = 'tu_clave_secreta'  # Cambia esto a una clave segura
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

# Ruta de registro de usuarios
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
    # Asegúrate de incluir el atributo 'foto' con un valor apropiado
    usuarios[cedula] = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'correo': correo,
        'contraseña': contraseña,
        'foto': 'nombre_de_archivo_de_foto.jpg'  # Reemplaza 'nombre_de_archivo_de_foto.jpg' con el nombre real de la foto
    }
    
    return render_template('inicio_sesion.html')


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    cedula = request.form.get('cedula')
    contraseña = request.form.get('contraseña')

    # Verificar las credenciales
    if cedula in usuarios:
        datos_usuario = usuarios[cedula]
        if datos_usuario['contraseña'] == contraseña:
            # Inicio de sesión exitoso, almacenar el nombre de usuario en la sesión
            session['usuario'] = cedula  # Puedes usar el número de cédula como identificador de usuario
            return redirect(url_for('perfil'))

    # Si las credenciales no coinciden, puedes mostrar un mensaje de error
    return render_template('inicio_sesion.html', error="Credenciales incorrectas")


@app.route('/perfil')
def perfil():
    # Obtén los datos del usuario de la sesión
    nombre_usuario = session.get('usuario')
    if nombre_usuario:
        datos_usuario = usuarios.get(nombre_usuario)
        if datos_usuario:
            return render_template('perfil.html', usuario=datos_usuario)  # Asegúrate de que 'usuario' se pase correctamente
    return redirect(url_for('inicio_sesion'))




if __name__ == '__main__':
    app.run(debug=True)
