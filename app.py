from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/generar", methods=["POST"])
def generar():
    # Capturar los valores del formulario
    tipo = request.form.get("tipo")
    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")
    adicional = request.form.get("adicional")

    # Armar el texto de solución final
    solucion = f"""
Tipo de solicitud: {tipo}
Nombre: {nombre}
Descripción: {descripcion}
Información adicional: {adicional if adicional else "N/A"}
"""

    # Pasar los datos como diccionario para la vista
    fields = {
        "Tipo de Solicitud": tipo,
        "Nombre": nombre,
        "Descripción": descripcion,
        "Solución Generada": solucion.strip()
    }

    return render_template("result.html", fields=fields)

if __name__ == "__main__":
    app.run(debug=True)
