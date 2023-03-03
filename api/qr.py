from flask import Flask, jsonify, request
import qrcode
from io import BytesIO

app = Flask(__name__)


@app.route('/qr', methods=['GET'])
def generate_qr():
    url = request.args.get('url')
    if url is None:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    # Create QR code image
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image to memory
    buf = BytesIO()
    img.save(buf, 'PNG')
    buf.seek(0)

    # Return image as response
    return app.response_class(buf.read(), content_type='image/png')


if __name__ == '__main__':
    app.run(debug=True)
