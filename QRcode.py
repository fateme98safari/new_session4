import qrcode
name=input("enter your name: ")
phone_number=input("enter your phone number: ")
img=qrcode.make(name + "|" +phone_number)
img.save("QRcode.png")