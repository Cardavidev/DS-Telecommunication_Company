from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('registro_usuario.html')  # Reemplaza 'tu_formulario.html' con la ruta correcta a tu formulario HTML

@app.route('/registrar', methods=['POST'])
def registrar():
    # Obtén los datos del formulario
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    cedula = request.form.get('cedula')
    telefono = request.form.get('telefono')
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')

    # Aquí puedes guardar los datos en un archivo local o en una base de datos
    # Por ejemplo, puedes guardarlos en un archivo CSV
    with open('clientes.csv', 'a') as file:
        file.write(f'{nombre},{apellido},{cedula},{telefono},{correo},{contraseña}\n')

    return render_template('inicio_sesion.html')

if __name__ == '__main__':
    app.run(debug=True)
