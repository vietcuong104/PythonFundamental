import pyqrcode
import png

link = "https://instagram.com/chengcheese/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)