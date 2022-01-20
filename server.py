from flask import Flask

app = Flask (__name__)

@app.route ('/')
def paginaInicial():
    return "¡Hola Mundo!"

@app.route ('/dojo')
def dojo():
    return "¡Dojo!"

@app.route ('/say/<name>')
def say(name):
    return f"¡Hola {name}!"

@app.route ('/repeat/<int:number>/<word>')
def repeat(number,word):
    return word * number

if __name__ == "__main__": #para que todo lo que se corra se ejecute directamente
    app.run( debug=True )