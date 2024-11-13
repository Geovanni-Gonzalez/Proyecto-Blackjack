from flask import Flask, render_template, request

app = Flask(__name__)

#Pagina principal
@app.route('/')
def inicio():
    return render_template('inicio.html')

#Pagina de juego
@app.route('/juego', methods=['GET', 'POST'])
def juego():
    nivel_dificultad = request.form['nivel_dificultad']
    modalidad = request.form['modalidad']
    
    return render_template('juego.html', nivel_dificultad=nivel_dificultad, modalidad=modalidad)

#Pagina de estadisticas
@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

#Pagina de modalidad
@app.route('/modalidad', methods=['GET', 'POST'])
def modalidad():
    return render_template('modalidad.html')

#Pagina de reglas
@app.route('/reglas')
def reglas():
    return render_template('reglas.html')  

if __name__ == '__main__':
    app.run(debug=True)