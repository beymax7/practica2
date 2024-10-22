from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', mostrar_menu=True)

@app.route('/curso', methods=['GET', 'POST'])
def curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return render_template('success.html', mensaje=f'Inscripción completada: {nombre} {apellidos}, Curso: {curso}', volver='curso', mostrar_menu=False)
    return render_template('curso.html', mostrar_menu=True)

@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        return render_template('success.html', mensaje=f'Registro de usuario completado: {nombre} {apellidos}, Correo: {correo}', volver='usuario', mostrar_menu=False)
    return render_template('usuario.html', mostrar_menu=True)

@app.route('/producto', methods=['GET', 'POST'])
def producto():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return render_template('success.html', mensaje=f'Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}', volver='producto', mostrar_menu=False)
    return render_template('producto.html', mostrar_menu=True)

@app.route('/libro', methods=['GET', 'POST'])
def libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return render_template('success.html', mensaje=f'Libro registrado: {titulo}, Autor: {autor}, Medio: {medio}', volver='libro', mostrar_menu=False)
    return render_template('libro.html', mostrar_menu=True)

if __name__ == '__main__':
    app.run(debug=True)
