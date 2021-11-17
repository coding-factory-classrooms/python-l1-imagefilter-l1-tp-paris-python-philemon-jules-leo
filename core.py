import cv2
from filtres import gray
from filtres import dilate
from filtres import blur
from pathlib import Path
import os


def apply_filters(images):
    for imgpath in images:
        gri = gray.gray_filter(imgpath)
        dil = dilate.dilate_filter(imgpath,5)
        blu = blur.blur_filter(imgpath,5)
        if not os.path.exists("output"):
            os.makedirs("output")
        cv2.imwrite("output/blurry.jpg", blu)
        cv2.imwrite("output/dilate.jpg", dil)
        cv2.imwrite("output/gray.jpg", gri)

def get_images(dir):
    """
    parcours le dossier et récupère les images
    :param dir: dossier à parcourir
    :return: une suite d'images du dossier
    """
    images = []
    pathlist = Path(dir).glob('**/*.jpg')
    for path in pathlist:
        image = str(path)
        images.append(image)
    return images

images = get_images('Images')
print(images)
apply_filters(images)
