import qrcode
url = qrcode.make("HELLO WORLD!!")
url.save('QRCODE.png')
