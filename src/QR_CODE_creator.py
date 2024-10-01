import qrcode

#Create an instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

#Ask for an URL
input = input("What would you like to convert?")
qr.add_data(input)

#Process URL and transform it into a QR code matrix // fit->to adjust the size of the qr to the data
qr.make(fit = True)

#Create the QR code image
image = qr.make_image(fill_color="black", back_color="white")


#Show the image in the terminal
qr.print_ascii()

#Save the image
image.save("QR_code_example.png")

#For further information look at other files