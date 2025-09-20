from flask import Flask, render_template, request, send_file
from openpyxl import Workbook
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        placa = request.form.get("placa")
        medio = request.form.get("medio")
        tipo = request.form.get("tipo")
        opcion = request.form.get("opcion")
        detalles = request.form.get("detalles")
        serial = request.form.get("serial")
        modelo = request.form.get("modelo")
        placa_equipo = request.form.get("placa_equipo")

        # Texto de salida base
        resultado = f"Medio: {medio}\nPlaca Equipo: {placa}\nCausa: {opcion}\n"

        # Si es alistamiento o reinstalación, añadimos datos extra
        if opcion in ["alistamiento", "reinstalacion"]:
            resultado += (
                f"Solución: {detalles}\n"
                f"Serial: {serial}\n"
                f"Modelo: {modelo}\n"
                f"Placa: {placa_equipo}"
            )
        else:
            resultado += f"Solución: {detalles}"

    return render_template("form.html", resultado=resultado)


@app.route("/download_txt", methods=["POST"])
def download_txt():
    output_text = request.form.get("output_text", "")
    file_stream = io.BytesIO(output_text.encode("utf-8"))
    file_stream.seek(0)

    return send_file(
        file_stream,
        as_attachment=True,
        download_name="formato.txt",
        mimetype="text/plain"
    )


@app.route("/download_excel", methods=["POST"])
def download_excel():
    output_text = request.form.get("output_text", "")

    # Dividir el texto en líneas y separarlas por ":"
    rows = []
    for line in output_text.splitlines():
        if ":" in line:
            campo, valor = line.split(":", 1)
            rows.append((campo.strip(), valor.strip()))

    # Crear Excel en memoria
    wb = Workbook()
    ws = wb.active
    ws.title = "Formato"

    # Encabezados
    ws.append(["Campo", "Valor"])

    # Insertar filas
    for campo, valor in rows:
        ws.append([campo, valor])

    # Guardar en memoria
    file_stream = io.BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return send_file(
        file_stream,
        as_attachment=True,
        download_name="formato.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


if __name__ == "__main__":
    app.run(debug=True)
