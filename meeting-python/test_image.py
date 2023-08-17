from PIL import Image

image = Image.open('meeting-python\\3.jpg')
coordinates = (100,200, image.width-100, image.height-100)
new_image = image.crop(coordinates)
new_image.save('meeting-python\\4.jpg')
print(image.size)
