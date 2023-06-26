from io import BytesIO
import qrcode
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/qr')
def generate_qr():
    url = request.args.get('url')
    size = int(request.args.get('size', 200))
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)