from flask import Flask, render_template, request

app = Flask(__name__)

# Opciones separadas por tipo
REQUERIMIENTOS = {
    "1": "Actualización y configuración de Ivanty VPN",
    "2": "Actualización Ivanty",
    "3": "Instalación y configuración OpenVPN",
    "4": "Permisos de administrador",
    "5": "Permisos de admin temporal",
    "6": "Revisión por retiro",
    "7": "Alistamiento"
}

INCIDENTES = {
    "1": "Error de Slack y Teams",
    "2": "Error de navegación Mac",
    "3": "Archivos dañados (Sonoma 14.4)"
}

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = ""
    if request.method == "POST":
        usuario = request.form["usuario"]
        placa = request.form["placa"]
        medio = "Presencial" if request.form["medio"] == "1" else "Virtual"
        tipo = "Requerimiento" if request.form["tipo"] == "req" else "Incidente"
        opcion = request.form["opcion"]
        detalles = request.form.get("detalles", "")

        # Buscar el texto según el tipo
        if tipo == "Requerimiento":
            causa = REQUERIMIENTOS[opcion]
        else:
            causa = INCIDENTES[opcion]

        # Armar el formato final
        resultado = (
            f"Tipo: {tipo}\n"
            f"Medio: {medio}\n"
            f"Placa Equipo: {placa}\n"
            f"Causa: {causa}\n"
            f"Solución: {detalles if detalles else '---'}\n"
            "¿Autoriza cierre del caso?: Si"
        )

    return render_template("form.html",
                           requerimientos=REQUERIMIENTOS,
                           incidentes=INCIDENTES,
                           resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


