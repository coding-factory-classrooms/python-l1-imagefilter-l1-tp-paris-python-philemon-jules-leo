import cv2


def gray_filter(img):
    """
    applique un filtre noir et blanc sur une image
    :param img: image à transformer
    :return: rien
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    return gray
