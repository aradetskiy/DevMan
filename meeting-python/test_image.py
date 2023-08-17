from PIL import Image

im = Image.open('meeting-python\\3.jpg')
red,gree, blue = im.split()
new_image = Image.merge('RGB',(red,gree, blue))
new_image.save('meeting-python\\4.jpg')
