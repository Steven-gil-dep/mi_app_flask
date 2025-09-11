from flask import Flask, render_template, request

app = Flask(__name__)

# Opciones separadas en requerimientos e incidentes
REQUERIMIENTOS = {
    1: "Actualización y configuración de Ivanty VPN",
    2: "Actualización Ivanty",
    4: "Instalación y configuración OpenVPN",
    16: "Permisos de administrador",
    18: "Permisos de admin temporal",
    19: "Revisión por retiro",
    20: "Alistamiento"
}

INCIDENTES = {
    3: "Falla en VPN",
    11: "Problemas de red",
    12: "Error en aplicaciones críticas"
    # agrega las demás que quieras
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        usuario = request.form.get("usuario")
        placa = request.form.get("placa")
        medio = request.form.get("medio")
        tipo = request.form.get("tipo")  # 'req' o 'inc'
        opcion = int(request.form.get("opcion"))
        detalles = request.form.get("detalles", "")

        # Medio traducido
        medio_txt = "Presencial" if medio == "1" else "Virtual"

        # Buscar la opción según el tipo
        if tipo == "req":
            causa = REQUERIMIENTOS.get(opcion, "No especificado")
            tipo_txt = "Requerimiento"
        else:
            causa = INCIDENTES.get(opcion, "No especificado")
            tipo_txt = "Incidente"

        # Resultado final
        resultado = f"""Tipo: {tipo_txt}
Medio: {medio_txt}
Placa Equipo: {placa}
Causa: {causa}
Solución: {detalles if detalles else 'N/A'}
¿Autoriza cierre del caso?: Si"""

    # Siempre enviar requerimientos e incidentes al template
    return render_template(
        "form.html",
        resultado=resultado,
        requerimientos=REQUERIMIENTOS,
        incidentes=INCIDENTES
    )

if __name__ == "__main__":
    app.run(debug=True)
