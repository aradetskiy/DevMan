from PIL import Image

im = Image.open('meeting-python\\3.jpg')

coord_left = (100, 0, im.width, im.height)
im_left = im.crop(coord_left)
coord_medium = (50,0,im.width-50,im.height)
im_medium = im.crop(coord_medium)
im_blend = Image.blend(im_medium,im_left,0.8)
im_blend.show()




