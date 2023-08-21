from PIL import Image
from os import remove

img = Image.open('meeting-python\monro.jpg')
red, green, blue = img.split()
shift = 20
red_shift_coordinates_left = (int(shift*2), 0, red.width, red.height)
red_shift_left = red.crop(red_shift_coordinates_left)
red_shift_coordinates_medium = (shift, 0, red.width-shift, red.height)
red_shift_medium = red.crop(red_shift_coordinates_medium)
red_new = Image.blend(red_shift_medium, red_shift_left, 0.7)

blue_shift_coordinates_right = (0, 0, int(blue.width-shift*2), blue.height)
blue_shift_right = blue.crop(blue_shift_coordinates_right)
blue_shift_coordinates_medium = (shift, 0, blue.width-shift, blue.height)
blue_shift_medium = blue.crop(blue_shift_coordinates_medium)
blue_new = Image.blend(blue_shift_medium, blue_shift_right, 0.7)

green_crop_coordinates = (shift, 0, green.width-shift, green.height)
green_new = green.crop(green_crop_coordinates)

new_img = Image.merge('RGB', (red_new, green_new, blue_new))
# remove('meeting-python\monro.jpg')
new_img.thumbnail((80, 80))
new_img.save('meeting-python\\avatar.jpg')
