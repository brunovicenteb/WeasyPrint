from flask import Flask, request, send_file
from weasyprint import HTML
import tempfile

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_html_to_pdf():
    html_data = request.get_data(as_text=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as pdf_file:
        HTML(string=html_data).write_pdf(pdf_file.name)
        return send_file(pdf_file.name, as_attachment=True, download_name="documento.pdf")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
