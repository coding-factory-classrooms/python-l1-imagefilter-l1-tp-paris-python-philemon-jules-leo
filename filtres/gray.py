import cv2


def gray_filter(img):
    """
    applique un filtre noir et blanc sur une image
    :param img: image à transformer
    :return: rien
    """
    fimage = cv2.imread(img)
    gray = cv2.cvtColor(fimage, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('Original image', fimage)
    cv2.imshow('image grise', gray)

    return gray

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.imwrite("jhgf.jpg", gray)