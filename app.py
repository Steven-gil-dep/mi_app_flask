from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        medio = request.form["medio"]
        placa = request.form["placa"]
        causa = request.form["causa"]
        solucion = (
            "Se realiza revisión del equipo mac con cargador,\n"
            "los cuales se encuentran físicamente con señales de uso común. "
            "Se realiza verificación\n"
            "del estado de los componentes de hardware como teclado, touchpad, Speaker, Pantalla, Puertos,\n"
            "Batería, Cámara y micrófono sin evidenciar anomalías en su funcionamiento. "
            "El equipo se encuentra en buen estado\n"
            "físico y funcional. Se realiza borrado seguro y eliminación del equipo del dominio."
        )
        autoriza = "Si"

        # Armamos el output tal cual lo necesitas
        output_text = (
            f"Medio: {medio}\n"
            f"Placa Equipo: {placa}\n"
            f"Causa: {causa}\n"
            f"Solución: {solucion}\n"
            f"¿Autoriza cierre del caso?: {autoriza}"
        )

        return render_template("result.html", output_text=output_text)

    return render_template("form.html")
