#pip install qrcode[pil]
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.
    ERROR_CORRECT_L,  #other contstants (M, Q, H)
    box_size=10,
    border=4,
)
print('Enter the path URL \n')
path = input()
qr.add_data(path)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
print('Enter file name ')
nameFile = input()
img.save(nameFile + '.png')
