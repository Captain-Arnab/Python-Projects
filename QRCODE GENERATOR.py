import qrcode
url = qrcode.make("www.youtube.com")
url.save('QRCODE.png')