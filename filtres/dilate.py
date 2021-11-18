import cv2
import numpy as np

def dilate_filter(img,pow):
    """
    applies a dilatation
    :param img: image
    :param pow: strength of the filter
    :return: input image with filter
    """
    kernel = np.ones((pow,pow),np.uint8)
    dilate = cv2.dilate(img, kernel, iterations=1)

    return dilate
