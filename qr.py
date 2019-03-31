import pyqrcode
from pyqrcode import QRCode

mensaje = 'Python en Español !!'

url = pyqrcode.create(mensaje)

url.svg('myqr.svg', scale= 8)