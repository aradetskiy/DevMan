from PIL import Image

image = Image.open('D:\\Develop\\DevMan\\meeting-python\\3.jpg')
new_image = image.convert('CMYK')
new_image.save('D:\\Develop\\DevMan\\meeting-python\\4.jpg')
