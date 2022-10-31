from email.mime import image
from captcha.image import ImageCaptcha
image  = ImageCaptcha()

data  = image.generate('ix05')

image.write('ix05','cap.png')