from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from base64 import b64decode

def generate_pdf(signature_data):
    signature_image_data = b64decode(signature_data.split(',')[1])

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.drawString(100, 100, "Hier ist die Unterschrift:")
    pdf.drawImage(signature_image_data, 100, 150)
    pdf.save()

    buffer.seek(0)
    return buffer
