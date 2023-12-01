from flask import Flask, render_template, request, send_file
from pdf_generator import generate_pdf
from pdf_generator import download_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/template/index.html')

@app.route('/download_pdf', methods=['GET', 'POST'])
def handle_pdf_download():
    return download_pdf()

if __name__ == '__main__':
    app.run(debug=True)
