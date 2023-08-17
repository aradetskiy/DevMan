from PIL import Image
from os import remove

im = Image.open('meeting-python\\monro.jpg')
im_rgb = im.convert('RGB')
print(
    f'Ширина  канала- {im.width} \nВысота  канала - {im.height}')
red, green, blue = im_rgb.split()
red.save('meeting-python\\monro_red.jpg')
green.save('meeting-python\\monro_green.jpg')
blue.save('meeting-python\\monro_blue.jpg')
# remove('meeting-python\\monro.jpg')
monro_new = Image.merge('RGB', (red, green, blue))

def change_channel(im,left_crop_width,left_crop_high,right_crop_width,right_crop_high):
    coord_channel_left = (left_crop_width, left_crop_high, right_crop_width, right_crop_high)
    im_left = im.crop(coord_channel_left)
    coord_channel_medium = (int(left_crop_width/2), left_crop_high, right_crop_width-int(left_crop_width/2), right_crop_high)
    im_medium = im.crop(coord_channel_medium)
    im_new = Image.blend(im_medium,im_left,0.7)
    
    return im_new


monro_red_new = change_channel(red,80,0,red.width,red.height)
print(
    f'Ширина красного канала- {monro_red_new.width} \nВысота красного канала - {monro_red_new.height}')
monro_blue_new = change_channel(blue,-80,0,red.width,red.height)
print(
    f'Ширина синего канала- {monro_blue_new.width} \nВысота синего канала - {monro_blue_new.height}')

monro_blue_new.show()

