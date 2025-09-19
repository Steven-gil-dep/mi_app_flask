from flask import Flask, render_template, request

app = Flask(__name__)

# Opciones con su "causa" y una "solución predefinida"
REQUERIMIENTOS = {
    1: ("Instalación y configuración de OpenVPN",
        "Se realizó la instalación y configuración del aplicativo OpenVPNConnect de manera satisfactoria, instalando los certificados actuales y el perfil de navegación requerido, verificando la correcta conexión y accesos."),
    2: ("Instalación de Sw (Individual)",
        "Se instala el aplicativo a satisfacción de manera correcta."),
    3: ("Instalación de Sw (Varios)",
        "Se realiza la instalación de los aplicativos requeridos a satisfacción de manera correcta."),
    4: ("Permisos de administrador",
        "Se otorgaron permisos de administrador temporal de acuerdo con la solicitud, y se dieron indicaciones al usuario."),
    5: ("Revisión por cambio de equipo",
        "Se realiza la revisión del equipo de cómputo, realizando pruebas de componentes de hardware como teclado, touchpad, pantalla, puertos, cámara, micrófono y speaker."),
    6: ("Revisión por retiro",
        "Se realizó la revisión del equipo por motivo de retiro, realizando pruebas de componentes de hardware como teclado, touchpad, pantalla, puertos, cámara, micrófono y speaker, sin evidenciar anomalías en su funcionamiento. Se realiza borrado seguro y eliminación del equipo de dominio."),
    7: ("Alistamiento",
        "Se realizó el alistamiento completo del equipo con cargador en buen estado físico y funcional, se adjuntan datos de la máquina y fotos."),
}

INCIDENTES = {
    1: ("Falla en VPN",
        "Se diagnosticó y corrigió la falla en el servicio VPN."),
    2: ("Problemas de red",
        "Se revisó la conectividad de red y se solucionaron los inconvenientes."),
    3: ("Error en aplicaciones críticas",
        "Se identificó y resolvió el error en la aplicación crítica reportada."),
    4: ("Reinstalación de OS",
        "Se reinstala el sistema operativo, se instalan los aplicativos básicos y se verifica que los agentes de seguridad queden reportando en su totalidad."),
    5: ("Error de inicio al OS (Windows)",
        "Se inicia sesión desde el usuario administrador local y se realiza comunicación con el servidor del dominio por medio de la red. Luego de esto, el inicio de sesión se realiza correctamente."),
    6: ("Restablecimiento Contraseña AWS",
        "Se cierra solicitud debido a que el área de soporte TI no cuenta con alcance ni administración de los accesos a AWS. Por favor generar solicitud por medio del canal de Slack #devops-faqs o en el tablero de Jira."),
}


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        # Datos principales
        placa = request.form.get("placa", "").strip()
        modelo = request.form.get("modelo", "").strip()
        serial = request.form.get("serial", "").strip()
        medio = request.form.get("medio")   # 1=presencial, 2=virtual
        tipo = request.form.get("tipo")     # 'req' o 'inc'
        opcion = int(request.form.get("opcion", "0"))
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

        # Agregar detalles adicionales si los hay
        if detalles:
            solucion += f" Detalles adicionales: {detalles}"

        # Mostrar datos de equipo solo en casos específicos
        if (tipo == "req" and opcion == 7) or (tipo == "inc" and opcion == 4):
            solucion += f"\nSerial: {serial}\nModelo: {modelo}\nPlaca: {placa}"

        # Resultado final
        resultado = f"""📋 Tipo: {tipo_txt}
🏢 Medio: {medio_txt}
💻 Placa Equipo: {placa}
🛠️ Causa: {causa}
✅ Solución: {solucion}

¿Autoriza cierre del caso?: Sí"""

    return render_template(
        "form.html",
        resultado=resultado,
        requerimientos={k: v[0] for k, v in REQUERIMIENTOS.items()},
        incidentes={k: v[0] for k, v in INCIDENTES.items()}
    )


if __name__ == "__main__":
    app.run(debug=True)



















