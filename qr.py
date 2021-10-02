import os 
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=8JnfIa84TnU")
img.save("solo-qr.png", "PNG")
os.system("start solo-qr.png")