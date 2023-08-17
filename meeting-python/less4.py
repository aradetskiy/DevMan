from PIL import Image
from os import remove

im = Image.open('meeting-python\\monro.jpg')
im_rgb=im.convert('RGB')
print(f'Ширина - {im_rgb.width} \nВысота - {im_rgb.height}\nЦветовая модель - {im_rgb.mode} ')
red,green,blue = im_rgb.split()
red.save('meeting-python\\monro_red.jpg')
green.save('meeting-python\\monro_green.jpg')
blue.save('meeting-python\\monro_blue.jpg')
remove('meeting-python\\monro.jpg')

monro_new = Image.merge('RGB',(red,green,blue))



monro_new.show()
