from flask import Flask, request, send_file
import PyPDF2
import io
from io import BytesIO

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert():
    pdf = request.args.get('pdf')
    # Open the PDF file
    pdfFile = open(pdf, 'rb')
    # Create a PDF reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    # Create a Word document object
    doc = io.StringIO()
    # Iterate over the pages of the PDF
    for pageNum in range(pdfReader.numPages):
        page = pdfReader.getPage(pageNum)
        # Extract the text from the page
        text = page.extractText()
        # Write the text to the Word document
        doc.write(text)
    # Set the file pointer to the beginning of the document
    doc.seek(0)
    # Create a response object with the Word document as the content
    response = send_file(
        doc,
        as_attachment=True,
        attachment_filename='converted.doc',
        mimetype='application/msword'
    )
    # Close the PDF file
    pdfFile.close()
    return response

if __name__ == '__main__':
    app.run()
