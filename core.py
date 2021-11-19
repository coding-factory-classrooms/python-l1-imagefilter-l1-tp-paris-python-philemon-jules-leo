import cv2
from PIL import Image

import logger as l
from filtres import grayscale
from filtres import dilate
from filtres import blur
from filtres import ZeTeam
from pathlib import Path
import os
import glob



def write_img(img_name, img, dir):
    cv2.imwrite(f'{dir}/{img_name}', img)

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
        l.log(f'Opening image = {img_path}')
        for f in filters:
            split = f.split(':')
            filter_name = split[0]
            if filter_name in ['grayscale', 'greyscale']:
                l.log(f'the grayscale filter has been successfully applied on the picture {name}')
                image = grayscale.gray_filter(image)
            elif filter_name == 'blur':
                if len(split) > 1 and split[1] != '' and int(split[1])%2 != 0:
                    pow = int(split[1])
                    l.log(f'the blur filter has been successfully applied on the picture {name} ')
                    image = blur.blur_filter(image, pow)
                else:
                    print('il manque le chiffre de puissance pour le filtre / il doit être impaire et positif')
            elif filter_name == 'dilate':
                if len(split) > 1:
                    l.log(f'the dilate filter has been successfully applied on the picture {name}')
                    pow = int(split[1])
                    image = dilate.dilate_filter(image, pow)
                else:
                    print('il manque un argument')
            elif filter_name == 'zeTeam':
                if len(split) > 1:
                    color = int(split[1], 16)
                    l.log(f'successfully applied zeTeam filter on {name}')
                    image = ZeTeam.zeTeam_filter(image,color)
        if not os.path.exists(odir):
            os.makedirs(odir)
        output_file = f"{odir}/{name}"
        cv2.imwrite(output_file, image)
        l.log(f'saving result image in {output_file}')



def get_images(fdir):
    """
    parcours le dossier et récupère les images
    :param fdir: dossier à parcourir
    :return: une suite d'images (chemin d'acces) du dossier
    """
    images = []
    pathlist = Path(fdir).glob('**/*.[jpg][png]*')
    for path in pathlist:
        image = str(path)
        images.append(image)
    return images

def get_video(dir, odir):

    frame_width = 640
    frame_height = 680

    if not os.path.exists(odir):
        os.makedirs(odir)

    cap = cv2.VideoCapture(dir)
    li = []
    y = 0
    i = 0


    while True:
        success, image = cap.read()
        if not success:
            break

        img = cv2.resize(image,(frame_width,frame_height))
        li.append(img)
        if i % 1 == 0:
            write_img(f'{odir}{y}.jpg', li[i],odir)
            y += 1
        i += 1

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


def get_image_video(dir):

    images = []
    pathlist = Path(dir).glob('**/*.[jpg][png]*')
    l.log('the images has been successfully taken')
    for path in pathlist:
        image = str(path)
        images.append(image)
    return images

def make_gif(odir, name):
    if os.path.exists(odir):
        frames = []
        for file in os.listdir(odir):
            with Image.open(f"{odir}/{file}").convert('P') as x:
                frames.append(x)
        frames[0].save(f'{name}.gif', format='GIF', append_images=frames[0:], save_all = True, duration= 300, loop=0)
    else:
        print("this directory don't exist")

