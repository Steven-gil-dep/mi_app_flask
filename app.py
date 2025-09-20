from flask import Flask, render_template, request

app = Flask(__name__)

# Opciones con su "causa" y una "solución predefinida"
REQUERIMIENTOS = {
    1: ("Instalacion y configuracion de OpenVPN",
        "Se realizó la Instalacion y configuración del aplicativo OpenVPNConnect de manera satisfactoria, se instalan los certificados actuales y el perfil de navegacion requerido verificando la correcta conexion y accesos"),
    2: ("instalacion de Sw(Individual)",
        "Se instala el aplicativo a satisfaccion de manera correcta."),
    3: ("Instalación de Sw(Varios)",
        "Se realiza la instalacion de los aplicativos requeridos a satisfaccion de manera correcta."),
    4: ("Permisos de administrador",
        "Se otorgaron permisos de administrador temporal comoros según la solicitud, y se le dan indicaciones al usuario"),
    5: ("Revicion por cambio de equipo",
        "Se realiza la revicion del equipo de computo, realizando pruebas de componentes de hardware com Teclado, Touchpad, pantalla, Puertos, Càmara, Microfono y Speaker."),
    6: ("Revisión por retiro",
        "Se realizó la revisión del equipo por motivo de retiro. realizando pruebas de componentes de hardware com Teclado, Touchpad, pantalla, Puertos, Càmara, Microfono y Speaker, sin evidenciar anomalìas en su funcionamiento durante las pruebas realizadas, se realiza borrado seguro y eliminacion del equipo de Dominio"),
    7: ("Alistamiento",
        "Se realizó el alistamiento completo del equipo con cargador en buen etsado fisico y funcionales, se adjuntos datos de la maquina y fotos."),
}

INCIDENTES = {
    1: ("Falla en VPN",
        "Se diagnosticó y corrigió la falla en el servicio VPN."),
    2: ("Problemas de red",
        "Se revisó la conectividad de red y se solucionaron los inconvenientes."),
    3: ("Error en aplicaciones críticas",
        "Se identificó y resolvió el error en la aplicación crítica reportada."),
    4: ("Reinstalacion de OS",
        "Se reinstala el sistema operativo, se instalan los aplicativos basicos y se verifica que los agentes de seguridad queden reportanto en su totalidad."),
    5: ("Error de inicio al OS (Para Wn)",
        "Se inicia sesion desde el usuario administrador Local y se realiza comunicacion con el servidor del dominio por medio de la red, luego de esto se inicia sesion correctamente."),
    6: ("Restablecimiento Contraseña AWS",
        "Se cierra solicitud debido a que el área de soporte TI no cuenta con alcance ni administración de los accesos a AWS, por favor generar solicitud por medio del canal de Slack #devops-faqs por tablero en Jira: https://avaldigitallabs.atlassian.net/jira/software/c/projects/OPS/boards/109."),
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        # Campos generales
        placa = request.form.get("placa")
        medio = request.form.get("medio")
        tipo = request.form.get("tipo")  # 'req' o 'inc'
        opcion = int(request.form.get("opcion"))
        detalles = request.form.get("detalles", "").strip()

        # Campos de equipo (para Alistamiento o Reinstalación)
        serial = request.form.get("serial", "").strip()
        modelo = request.form.get("modelo", "").strip()
        placa_equipo = request.form.get("placa_equipo", "").strip()

        # Medio traducido
        medio_txt = "Presencial" if medio == "1" else "Virtual"

        # Buscar la opción según el tipo
        if tipo == "req":
            causa, solucion = REQUERIMIENTOS.get(opcion, ("No especificado", ""))
            tipo_txt = "Requerimiento"
        else:
            causa, solucion = INCIDENTES.get(opcion, ("No especificado", ""))
            tipo_txt = "Incidente"

        # Agregar detalles
        if detalles:
            solucion = f"{solucion}\nDetalles adicionales: {detalles}"

        # Agregar datos de equipo solo si aplica
        if "Alistamiento" in causa or "Reinstalacion" in causa:
            solucion = f"""{solucion}
Serial: {serial}
Modelo: {modelo}
Placa: {placa_equipo}"""

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
