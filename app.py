from flask import Flask, render_template, request, send_file
from pdf_generator import generate_pdf

app = Flask(__name__)

@app.route('/download_pdf', methods=['GET', 'POST'])

def download_pdf():
   
    print("Route '/download_pdf' wurde aufgerufen.")
    
    if request.method == 'POST':
        print("POST-Anfrage empfangen.")
        
        signature_data = request.form['signature']
        print("Unterschriftdaten erhalten:", signature_data)

    pdf_buffer = generate_pdf(signature_data)
    pdf_buffer.seek(0)

    # Sende die PDF-Datei zurück als Downloada
    return send_file(
        pdf_buffer,
        as_attachment=True,
        attachment_filename='convertPDF.pdf',
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
