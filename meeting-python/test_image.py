from PIL import Image

im = Image.open('meeting-python\\3.jpg')

width,high = im.size

print(im.size)
new_size = (int(width/2), int(high/2))
new_im = im.resize(new_size)
#im.thumbnail((1200, 768))
print(new_im.size)
new_im.show()

