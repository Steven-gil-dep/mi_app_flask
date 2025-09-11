from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Tomar los datos del formulario
        tipo = request.form.get("tipo", "").strip()
        nombre = request.form.get("nombre", "").strip()
        descripcion = request.form.get("descripcion", "").strip()
        adicional = request.form.get("adicional", "").strip()

        # Construir campos para enviar al template
        fields = {
            "📌 Tipo de Solicitud": tipo or "(sin especificar)",
            "👤 Nombre del Solicitante": nombre or "(sin nombre)",
            "📝 Descripción": descripcion or "(sin descripción)",
            "📎 Información adicional": adicional or "(ninguna)"
        }

        return render_template("result.html", fields=fields)

    # Si es GET, muestra el formulario
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
