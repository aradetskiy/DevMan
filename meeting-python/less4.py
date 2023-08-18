from PIL import Image
from os import remove

img = Image.open('meeting-python\\monro.jpg')
img_rgb = img.convert('RGB')
red, green, blue = img_rgb.split()
remove('meeting-python\\monro.jpg')


def shadow_image(img, count_shift, img_width, img_height, unvisibility_shadow):
    if count_shift > 0:
        img_coord_right = (0, 0, img_width - int(count_shift*2), img_height)
        img_right = img.crop(img_coord_right)
        img_coord_medium = (count_shift, 0, img_width-count_shift, img_height)
        img_medium = img.crop(img_coord_medium)
        img_new = Image.blend(img_medium, img_right, unvisibility_shadow)
    else:
        count_shift = abs(count_shift)
        img_coord_left = (int(count_shift*2), 0, img_width, img_height)
        img_left = img.crop(img_coord_left)
        img_coord_medium = (count_shift, 0, int(img_width-count_shift), img_height)
        img_medium = img.crop(img_coord_medium)
        img_new = Image.blend(img_medium, img_left, unvisibility_shadow)
    return img_new

# count_shift_shadow -  count pixel to move shadow.
# If you want move shadow right you should choose positive integer number
# If you want move shadow left you should choose negаtive integer number


count_shift_shadow = 10
# if want increase visibility shadow you should decrease unvisibility_shadow
unvisibility_shadow = 0.7

monro_red_new = shadow_image(
    red, count_shift_shadow, red.width, red.height, unvisibility_shadow)

monro_blue_new = shadow_image(
    blue, -count_shift_shadow, blue.width, blue.height, unvisibility_shadow)

coord_monro_green_new = (count_shift_shadow, 0, int(
    green.width-count_shift_shadow), green.height)
monro_green_new = green.crop(coord_monro_green_new)


monro_shadow = Image.merge(
    'RGB', (monro_red_new, monro_blue_new, monro_green_new))

monro_shadow.thumbnail((80, 80))
monro_shadow.save('meeting-python\\monro_avatar.jpg')
