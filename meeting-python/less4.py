from PIL import Image
from os import remove

im = Image.open('meeting-python\\monro.jpg')
im_rgb = im.convert('RGB')
red, green, blue = im_rgb.split()
# red.save('meeting-python\\monro_red.jpg')
# green.save('meeting-python\\monro_green.jpg')
# blue.save('meeting-python\\monro_blue.jpg')
# remove('meeting-python\\monro.jpg')
monro_new = Image.merge('RGB', (red, green, blue))

def shadow_image(im, count_move, im_width, im_height):
    if count_move > 0:
        im_coord_right = (0, 0, im_width - int(count_move*2), im_height)
        im_right = im.crop(im_coord_right)
        im_coord_medium = (count_move, 0, im_width-count_move, im_height)
        im_medium = im.crop(im_coord_medium)
        im_new = Image.blend(im_medium, im_right, 0.7)
    else:
        count_move = abs(count_move)
        im_coord_left = (int(count_move*2), 0, im_width, im_height)
        im_left = im.crop(im_coord_left)
        im_coord_medium = (count_move, 0, int(im_width-count_move), im_height)
        im_medium = im.crop(im_coord_medium)
        im_new = Image.blend(im_medium, im_left, 0.7)
    return im_new

count_move_shadow = 10  # count pixel to move shadow

monro_red_new = shadow_image(
    red, count_move_shadow, red.width, red.height)


monro_blue_new = shadow_image(
    blue, -count_move_shadow, blue.width, blue.height)


coord_monro_green_new = (count_move_shadow, 0, int(
    green.width-count_move_shadow), green.height)
monro_green_new = green.crop(coord_monro_green_new)



monro_shadow = Image.merge('RGB',(monro_red_new,monro_blue_new,monro_green_new))
monro_shadow.thumbnail((80,80))
monro_shadow.show()
print(
    f'Ширина красного канала- {monro_red_new.width}\nШирина синего канала- {monro_blue_new.width} \nШирина зеленого канала- {monro_green_new.width}\nАватарка - {monro_shadow.size}')