from PIL import Image

image = Image.open('meeting-python\\3.jpg')
new_image = image.rotate(45)
new_image.show()
#new_image.save('meeting-python\\4.jpg')
