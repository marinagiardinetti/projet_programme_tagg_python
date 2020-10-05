from PIL import Image
from resizeimage import resizeimage
 
with open('origine_1000.png', 'r') as f:
    TAILLE = [800, 700]
    FIXE = 400
    img = Image.open(f)
    img = resizeimage.resize_crop(img, TAILLE)
    img.save('crop.png', img.format)