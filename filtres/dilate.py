import cv2
import numpy as np

def dilate_filter(img,pow):
    kernel = np.ones((pow,pow),np.uint8)
    fimage = cv2.imread(img)
    dilate = cv2.dilate(fimage, kernel, iterations=1)

    # cv2.imshow('Original image', fimage)
    cv2.imshow('image dilatée', dilate)

    return dilate

    cv2.waitKey(0)
    cv2.destroyAllWindows()