from flask import Flask, render_template_string, request

app = Flask(__name__)

REQUERIMIENTOS = {
    1: "Actualización y configuración de Ivanty VPN",
    2: "Actualización Ivanty",
    3: "Instalación y configuración OpenVPN",
    4: "Permisos de administrador",
    5: "Permisos de admin temporal",
    6: "Revisión por retiro",
    7: "Alistamiento"
}

INCIDENTES = {
    1: "Inicio de sesión usuario local",
    2: "Error de Slack y Teams",
    3: "Error de navegación Mac",
    4: "Cambio de contraseña DA",
    5: "Archivos dañados (Sonoma 14.4)"
}

HTML_FORM = """<!DOCTYPE html>
<html>
<head>
    <title>Generador de Formato</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        label { display:block; margin-top:10px; }
        select, input, textarea { width: 100%%; padding: 8px; margin-top: 5px; }
        button { margin-top: 15px; padding: 10px 15px; background:#007bff; color:white; border:none; cursor:pointer; }
        pre { background:#f4f4f4; padding:10px; border-radius:5px; }
    </style>
</head>
<body>
    <h1>Generador de Formato de Cierre</h1>
    <form method="post">
        <label>Nombre del usuario:</label>
        <input type="text" name="usuario" required>

        <label>Placa del equipo:</label>
        <input type="text" name="placa" required>

        <label>Medio:</label>
        <select name="medio" required>
            <option value="Presencial">Presencial</option>
            <option value="Virtual">Virtual</option>
        </select>

        <label>Tipo:</label>
        <select name="tipo" required onchange="this.form.submit()">
            <option value="">-- Selecciona --</option>
            <option value="Requerimiento">Requerimiento</option>
            <option value="Incidente">Incidente</option>
        </select>

        {% if opciones %}
            <label>Opciones de {{ tipo }}:</label>
            <select name="opcion" required>
            {% for idx, causa in opciones.items() %}
                <option value="{{ idx }}">{{ idx }}) {{ causa }}</option>
            {% endfor %}
            </select>

            <label>Detalles adicionales (opcional):</label>
            <textarea name="detalles"></textarea>

            <button type="submit">Generar Formato</button>
        {% endif %}
    </form>

    {% if resultado %}
        <h2>Formato generado:</h2>
        <pre>{{ resultado }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    opciones = None
    resultado = None
    tipo = None

    if request.method == "POST":
        usuario = request.form.get("usuario")
        placa = request.form.get("placa")
        medio = request.form.get("medio")
        tipo = request.form.get("tipo")
        opcion = request.form.get("opcion")
        detalles = request.form.get("detalles", "")

        if tipo == "Requerimiento":
            opciones = REQUERIMIENTOS
        elif tipo == "Incidente":
            opciones = INCIDENTES

        if opcion:
            causa = opciones[int(opcion)]
            resultado = f"""
Medio: {medio}
Placa Equipo: {placa}
Tipo: {tipo}
Causa: {causa}
Solución: {causa}. {detalles}
¿Autoriza cierre del caso?: Sí
"""

    return render_template_string(HTML_FORM, opciones=opciones, resultado=resultado, tipo=tipo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
