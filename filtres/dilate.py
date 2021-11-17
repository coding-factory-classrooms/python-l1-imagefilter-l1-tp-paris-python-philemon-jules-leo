import cv2
import numpy as np

def dilate_filter(img,pow):
    kernel = np.ones((pow,pow),np.uint8)
    dilate = cv2.dilate(img, kernel, iterations=1)

    return dilate
