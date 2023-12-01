import os
from flask import request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from base64 import b64decode
import tempfile

def generate_pdf(signature_data, file_path):
    # Dekodieren der Bilddaten
    signature_image_data = b64decode(signature_data.split(',')[1])

    # Speichern der Bilddaten in einer temporären Datei
    with tempfile.NamedTemporaryFile(delete=False) as temp_image_file:
        temp_image_file.write(signature_image_data)

    # Erstellen der PDF-Datei
    pdf = canvas.Canvas(file_path, pagesize=letter)
    pdf.drawString(100, 100, "Hier ist die Unterschrift:")
    pdf.drawImage(temp_image_file.name, 100, 150)  # Verwenden des temporären Dateipfades
    pdf.save()

    # Löschen der temporären Bilddatei
    os.remove(temp_image_file.name)

def download_pdf():
    print("Route '/download_pdf' wurde aufgerufen.")
    signature_data = request.form['signature']
    if request.method == 'POST':
        print("POST-Anfrage empfangen.")
        print("Unterschriftdaten erhalten:", signature_data)

    # Pfad für die Speicherung der PDF-Datei
    file_path = os.path.join('static', 'fileAblage', 'unterschrift.pdf')

    # Erstellen der PDF-Datei
    generate_pdf(signature_data, file_path)

    # Sende die PDF-Datei zurück als Download
    return send_file(
        file_path,
        as_attachment=True,
        mimetype='application/pdf',
        download_name='unterschrift.pdf'
    )
