from flask import Flask, render_template, request

app = Flask(__name__)

# Opciones con su "causa" y una "solución predefinida"
REQUERIMIENTOS = {
    1: ("Instalacion y configuracion de OpenVPN",
        "Se realizó la Instalacion y configuración del aplicativo OpenVPNConnect de manera satisfactoria, se instalan los certificados actuales y el perfil de navegacion requerido verificando la correcta conexion y accesos"),
    2: ("instalacion de Sw(Individual)",
        "Se instala el aplicativo a satisfaccion de manera correcta."),
    4: ("Instalación de Sw(Varios)",
        "Se realiza la instalacion de los aplicativos requeridos a satisfaccion de manera correcta."),
    16: ("Permisos de administrador",
        "Se otorgaron permisos de administrador temporal comoros según la solicitud, y se le dan indicaciones al usuario"),
    18: ("",
        "Se concedieron permisos de administrador temporales."),
    19: ("Revisión por retiro",
        "Se realizó la revisión del equipo por motivo de retiro."),
    20: ("Alistamiento",
        "Se realizó el alistamiento completo del equipo con cargador, se adjuntos datos de la maquina y fotos.")
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

