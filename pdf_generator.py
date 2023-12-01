from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from base64 import b64decode
from flask import request, send_file

def generate_pdf(signature_data):
    signature_image_data = b64decode(signature_data.split(',')[1])

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.drawString(100, 100, "Hier ist die Unterschrift:")
    pdf.drawImage(signature_image_data, 100, 150)
    pdf.save()

    buffer.seek(0)
    return buffer

def download_pdf():
   
    print("Route '/download_pdf' wurde aufgerufen.")
    
    if request.method == 'POST':
        print("POST-Anfrage empfangen.")
        
        signature_data = request.form['signature']
        print("Unterschriftdaten erhalten:", signature_data)

    pdf_buffer = generate_pdf(signature_data)
    pdf_buffer.seek(0)

    # Sende die PDF-Datei zurück als Download
    return send_file(
        pdf_buffer,
        as_attachment=True,
        attachment_filename='convertPDF.pdf',
        mimetype='application/pdf'
    )