import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://www.linkedin.com/in/hamza-rafique-developer/")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="blue")

img.save("hamza-rafique-linkdin-advance.png")