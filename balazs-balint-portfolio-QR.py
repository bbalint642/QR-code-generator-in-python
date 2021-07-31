import qrcode

qr = qrcode.QRCode(
    version=2,
    box_size=12,
    border=3
    )

data = 'https://balint-balazs-portfolio-site.netlify.app/'

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('Portfolio site QR Code.png')
