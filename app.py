from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tipo = request.form["tipo"]
        descripcion = request.form["descripcion"]
        adicional = request.form["solucion"]

        # Armamos el texto completo como antes (en Solución)
        solucion = f"""Se recibe {tipo.lower()} con la siguiente descripción:
{descripcion}

Acciones realizadas:
{adicional}
"""

        fields = {
            "Tipo": tipo,
            "Descripción": descripcion,
            "Solución": solucion.strip()
        }

        return render_template("result.html", fields=fields)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
