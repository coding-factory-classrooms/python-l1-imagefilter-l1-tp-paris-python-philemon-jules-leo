import cv2
from PIL import Image

import logger as l
from filtres import gray
from filtres import dilate
from filtres import blur
from filtres import ZeTeam
from pathlib import Path
import os
import glob




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
                if len(split) > 1:
                    color = int(split[1], 16)
                    l.log(f'successfully applied zeTeam filter on {name}')
                    image = ZeTeam.zeTeam_filter(image,color)
        if not os.path.exists(odir):
            os.makedirs(odir)
        output_file = f"{odir}/{name}"
        cv2.imwrite(output_file, image)

def get_images(fdir):
    """
    parcours le dossier et récupère les images
    :param fdir: dossier à parcourir
    :return: une suite d'images (chemin d'acces) du dossier
    """
    images = []
    pathlist = Path(fdir).glob('**/*.[jpg][png]*')
    l.log('the images has been successfully taken')
    for path in pathlist:
        image = str(path)
        images.append(image)
    return images

def get_video(dir):

    cap = cv2.VideoCapture(dir)

    if not os.path.exists('output_video'):
        os.makedirs('output_video')

    current_frame = 0

    FPS = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    bool = True
    while(bool):

        ret, frame = cap.read()

        name = './output_video/frame' + str(current_frame) + '.jpg'
        print('Creating...' + name)
        print(ret)
        bool = ret
        try:
            cv2.imwrite(name, frame)
        except:
            continue

        current_frame += 1



def get_image_video(dir):

    images = []
    pathlist = Path(dir).glob('**/*.[jpg][png]*')
    l.log('the images has been successfully taken')
    for path in pathlist:
        image = str(path)
        images.append(image)
    return images

def make_gif(odir):
    frames = [Image.open(image) for image in glob.glob(f"{odir}/*.jpg")]
    frame_one = frames[0]
    frame_one.save("filtered_images.gif", format="GIF", append_images=frames,
                   save_all=True, duration=1000, loop=0)

