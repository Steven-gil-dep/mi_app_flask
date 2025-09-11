from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario de soluciones predefinidas
SOLUCIONES = {
    "Actualización y configuración de Ivanty VPN": "Se realizó la actualización y configuración de Ivanty VPN garantizando la correcta conexión.",
    "Actualización Ivanty": "Se actualizó la aplicación Ivanty a la última versión disponible.",
    "Instalación y configuración OpenVPN": "Se instaló y configuró el cliente OpenVPN dejando establecida la conexión.",
    "Permisos de administrador": "Se otorgaron permisos de administrador al usuario para ejecutar las tareas requeridas.",
    "Permisos de admin temporal": "Se habilitaron permisos de administrador temporalmente para la actividad solicitada.",
    "Revisión por retiro": "Se realizó la revisión completa del equipo para proceso de retiro.",
    "Alistamiento": "Se efectuó el alistamiento del equipo para su correcto funcionamiento.",
    # Ejemplo de incidentes
    "Falla de red": "Se diagnosticó y solucionó la falla de conectividad de red.",
    "Error de sistema operativo": "Se corrigió el error del sistema operativo asegurando el arranque correcto."
}

# Opciones separadas
REQUERIMIENTOS = [
    "Actualización y configuración de Ivanty VPN",
    "Actualización Ivanty",
    "Instalación y configuración OpenVPN",
    "Permisos de administrador",
    "Permisos de admin temporal",
    "Revisión por retiro",
    "Alistamiento"
]

INCIDENTES = [
    "Falla de red",
    "Error de sistema operativo"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        placa = request.form.get("placa", "").strip()
        medio = request.form.get("medio", "").strip()
        tipo = request.form.get("tipo", "").strip()
        opcion = request.form.get("opcion", "").strip()
        adicional = request.form.get("adicional", "").strip()

        # Buscar solución en el diccionario
        solucion_base = SOLUCIONES.get(opcion, "No se encontró una solución definida para esta opción.")
        # Agregar info adicional si existe
        solucion_final = solucion_base
        if adicional:
            solucion_final += f"\nNota adicional: {adicional}"

        fields = {
            "Tipo": tipo,
            "Medio": medio,
            "Placa Equipo": placa,
            "Usuario": usuario,
            "Causa": opcion,
            "Solución": solucion_final,
            "¿Autoriza cierre del caso?": "Si"
        }

        return render_template("result.html", fields=fields)

    return render_template("form.html", requerimientos=REQUERIMIENTOS, incidentes=INCIDENTES)

if __name__ == "__main__":
    app.run(debug=True)
