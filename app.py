from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/generar", methods=["POST"])
def generar():
    usuario = request.form.get("usuario")
    placa = request.form.get("placa")
    medio = request.form.get("medio")
    tipo = request.form.get("tipo")
    opcion = request.form.get("opcion")
    adicional = request.form.get("adicional")

    # La solución se arma como antes
    solucion = f"{opcion}. {adicional}" if adicional else opcion

    return render_template("result.html",
                           tipo=tipo,
                           medio=medio,
                           placa=placa,
                           opcion=opcion,
                           solucion=solucion)

if __name__ == "__main__":
    app.run(debug=True)
