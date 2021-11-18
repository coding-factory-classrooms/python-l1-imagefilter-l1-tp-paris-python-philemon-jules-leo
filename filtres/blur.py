import cv2

def blur_filter(img,pow):
    """
    fonction appliquant le filtre blur
    :param img: l'image sur laquelle appliquer le filtre
    :param pow: la puissance du blur
    :return: retourne l'image filtré
    """
    blur = cv2.GaussianBlur(img, (pow,pow),cv2.BORDER_DEFAULT)


    return blur


