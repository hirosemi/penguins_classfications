import os
import sys
from PIL import Image, ImageDraw, ImageFont


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def resize_image_with_pad(im, new_width, new_height):
    crop_size = im.height if im.height >= im.width else im.width
    img = crop_center(im, crop_size, crop_size)
    return img.resize((new_width, new_height), Image.LANCZOS)

def genResize(img_file, img_size, outdirpath):
    filename = os.path.basename(img_file)
    (fn, ext) = os.path.splitext(filename)

    outpath = os.path.join(outdirpath, "%s_%d%s" % (fn, img_size, ext))
#    print(outpath)
    im = Image.open(img_file)
    print("%s size %d %d " % (filename, im.width, im.height))
    imr = resize_image_with_pad(im, img_size, img_size)
    imr.save(outpath)

def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    
if __name__ == "__main__":
    param = sys.argv
    dirname = os.path.basename(os.path.normpath(param[1]))
    outdirpath = os.path.join('./resize', dirname)
    make_dir(outdirpath)
    
    directory = os.listdir(os.path.normpath(param[1]))
    for imgFile in directory:
        genResize(os.path.join(param[1], imgFile), 128, outdirpath)


