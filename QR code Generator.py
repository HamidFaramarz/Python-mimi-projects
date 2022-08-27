import pyqrcode
#import the lib
from pyqrcode import QRCode
#the link that you want to generate qr code
link = "https://github.com/HamidFaramarz"

# the generation part 
URL_gener = pyqrcode.create(link)

# save the oup as picture
URL_gener.svg("github.svg", scale=10)