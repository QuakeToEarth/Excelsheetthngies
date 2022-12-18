import pyqrcode
import png
from pyqrcode import QRCode
s = "Kfc Chicken"
url = pyqrcode.create(s)
# url.svg('Alicia.svg', scale = 8)
url.png("myqr.png",scale = 6)
