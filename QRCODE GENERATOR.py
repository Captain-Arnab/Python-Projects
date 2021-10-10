import pyqrcode

url = pyqrcode.create("HELLO WORLD!!")
url.png("QRCODE.png",scale=20)

