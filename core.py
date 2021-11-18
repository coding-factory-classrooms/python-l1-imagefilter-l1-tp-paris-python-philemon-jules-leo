import cv2

import logger as l
from filtres import gray
from filtres import dilate
from filtres import blur
from filtres import ZeTeam
from pathlib import Path
import os


def apply_filters(images, odir, filters):
    """
    applies filters on images from input file and writes the result in an output directory
    :param images: array of images/path
    :param odir: output file
    :param filters: filters to be applied
    :return: nothing
    """
    for img_path in images:
        image = cv2.imread(img_path)
        name = os.path.basename(img_path)
        for f in filters:
            split = f.split(':')
            filter_name = split[0]
            if filter_name in ['grayscale', 'greyscale']:
                l.log(f'the grayscale filter has been successfully applied on the picture {name}')
                image = gray.gray_filter(image)
            elif filter_name == 'blur':
                if len(split) > 1:
                    pow = int(split[1])
                    l.log(f'the blur filter has been successfully applied on the picture {name} ')
                    image = blur.blur_filter(image, pow)
                else:
                    print('il manque un argument')
            elif filter_name == 'dilate':
                if len(split) > 1:
                    l.log(f'the dilate filter has been successfully applied on the picture {name}')
                    pow = int(split[1])
                    image = dilate.dilate_filter(image, pow)
                else:
                    print('il manque un argument')
            elif filter_name == 'zeTeam':
                l.log(f'successfully applied zeTeam filter on {name}')
                image = ZeTeam.zeTeam_filter(image)


        # gri = gray.gray_filter(image)
        # dil = dilate.dilate_filter(gri,5)
        # blur_size = 5
        # try:
        #     blu = blur.blur_filter(dil, blur_size)
        #     cv2.imwrite("output/blurry.jpg", blu)
        # except cv2.error as e:
        #     print(f'Even blur value detected. Actual value = {blur_size}. Suggested value: {blur_size + 1}')
        if not os.path.exists(odir):
            os.makedirs(odir)
        output_file = f"{odir}/{name}"
        cv2.imwrite(output_file, image)

def get_images(fdir):
    """
    parcours le dossier et récupère les images
    :param dir: dossier à parcourir
    :return: une suite d'images du dossier
    """
    images = []
    pathlist = Path(fdir).glob('**/*.[jpg][png]*')
    l.log('the images has been successfully taken')
    for path in pathlist:
        image = str(path)
        images.append(image)
    return images

# images = get_images('Images')
# print(images)
# apply_filters(images)
