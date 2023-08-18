from PIL import Image
from os import remove

im = Image.open('meeting-python\\monro.jpg')
im_rgb = im.convert('RGB')
red, green, blue = im_rgb.split()
remove('meeting-python\\monro.jpg')


def shadow_image(im, count_move, im_width, im_height, unvisibility_shadow):
    if count_move > 0:
        im_coord_right = (0, 0, im_width - int(count_move*2), im_height)
        im_right = im.crop(im_coord_right)
        im_coord_medium = (count_move, 0, im_width-count_move, im_height)
        im_medium = im.crop(im_coord_medium)
        im_new = Image.blend(im_medium, im_right, unvisibility_shadow)
    else:
        count_move = abs(count_move)
        im_coord_left = (int(count_move*2), 0, im_width, im_height)
        im_left = im.crop(im_coord_left)
        im_coord_medium = (count_move, 0, int(im_width-count_move), im_height)
        im_medium = im.crop(im_coord_medium)
        im_new = Image.blend(im_medium, im_left, unvisibility_shadow)
    return im_new

# count_move_shadow -  count pixel to move shadow.
# If you want move shadow right you should choose positive integer number
# If you want move shadow left you should choose negtive integer number


count_move_shadow = 10
# if want increase visibility shadow you should decrease unvisibility_shadow
unvisibility_shadow = 0.7

monro_red_new = shadow_image(
    red, count_move_shadow, red.width, red.height, unvisibility_shadow)

monro_blue_new = shadow_image(
    blue, -count_move_shadow, blue.width, blue.height, unvisibility_shadow)

coord_monro_green_new = (count_move_shadow, 0, int(
    green.width-count_move_shadow), green.height)
monro_green_new = green.crop(coord_monro_green_new)


monro_shadow = Image.merge(
    'RGB', (monro_red_new, monro_blue_new, monro_green_new))

monro_shadow.thumbnail((80, 80))
monro_shadow.save('meeting-python\\monro_avatar.jpg')
