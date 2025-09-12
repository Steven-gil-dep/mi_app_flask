from flask import Flask, render_template, request

app = Flask(__name__)

# Opciones con su "causa" y una "solución predefinida"
REQUERIMIENTOS = {
    1: ("Actualización y configuración de Ivanty VPN",
        "Se realizó la actualización y configuración de Ivanty VPN de manera satisfactoria."),
    2: ("Actualización Ivanty",
        "Se ejecutó la actualización de Ivanty correctamente."),
    4: ("Instalación y configuración OpenVPN",
        "Se instaló y configuró OpenVPN garantizando la conectividad."),
    16: ("Permisos de administrador",
        "Se otorgaron permisos de administrador según la solicitud."),
    18: ("Permisos de admin temporal",
        "Se concedieron permisos de administrador temporales."),
    19: ("Revisión por retiro",
        "Se realizó la revisión del equipo por motivo de retiro."),
    20: ("Alistamiento",
        "Se realizó el alistamiento completo del equipo.")
}

INCIDENTES = {
    3: ("Falla en VPN",
        "Se diagnosticó y corrigió la falla en el servicio VPN."),
    11: ("Problemas de red",
        "Se revisó la conectividad de red y se solucionaron los inconvenientes."),
    12: ("Error en aplicaciones críticas",
        "Se identificó y resolvió el error en la aplicación crítica reportada.")
    # Puedes seguir agregando más
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
        detalles = request.form.get("detalles", "").strip()

        # Medio traducido
        medio_txt = "Presencial" if medio == "1" else "Virtual"

        # Buscar la opción según el tipo
        if tipo == "req":
            causa, solucion = REQUERIMIENTOS.get(opcion, ("No especificado", ""))
            tipo_txt = "Requerimiento"
        else:
            causa, solucion = INCIDENTES.get(opcion, ("No especificado", ""))
            tipo_txt = "Incidente"

        # Agregar detalles si los hay
        if detalles:
            solucion = f"{solucion} Detalles adicionales: {detalles}"

        # Resultado final
        resultado = f"""Tipo: {tipo_txt}
Medio: {medio_txt}
Placa Equipo: {placa}
Causa: {causa}
Solución: {solucion}
¿Autoriza cierre del caso?: Si"""

    return render_template(
        "form.html",
        resultado=resultado,
        requerimientos={k: v[0] for k, v in REQUERIMIENTOS.items()},
        incidentes={k: v[0] for k, v in INCIDENTES.items()}
    )

if __name__ == "__main__":
    app.run(debug=True)
