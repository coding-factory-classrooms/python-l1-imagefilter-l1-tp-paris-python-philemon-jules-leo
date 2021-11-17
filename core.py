import cv2
from filtres import gray
from filtres import dilate
from filtres import blur
from pathlib import Path
import os


def apply_filters(images,odir):

    for imgpath in images:
        image = cv2.imread(imgpath)
        gri = gray.gray_filter(image)
        dil = dilate.dilate_filter(gri,5)
        blur_size = 5
        try:
            blu = blur.blur_filter(dil, blur_size)
            cv2.imwrite("output/blurry.jpg", blu)
        except cv2.error as e:
            print(f'Even blur value detected. Actual value = {blur_size}. Suggested value: {blur_size + 1}')
        if not os.path.exists("output"):
            os.makedirs("output")
        if not os.path.exists(odir):
            os.makedirs(odir)
        name = os.path.basename(imgpath)
        cv2.imwrite(f"output/{name}", blu)

def get_images(fdir):
    """
    parcours le dossier et récupère les images
    :param dir: dossier à parcourir
    :return: une suite d'images du dossier
    """
    images = []
    pathlist = Path(fdir).glob('**/*.[jpg][png]*')
    for path in pathlist:
        image = str(path)
        images.append(image)
    return images

# images = get_images('Images')
# print(images)
# apply_filters(images)
