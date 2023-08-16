from PIL import Image

image = Image.open('D:\Develop\DevMan\meeting-python\\1.png')
rotated_image = image.rotate(45)
rotated_image.save('D:\Develop\DevMan\meeting-python\\2.png')