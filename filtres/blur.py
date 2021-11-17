import cv2

def blur_filter(img,pow):
    blur = cv2.GaussianBlur(img, (pow,pow),cv2.BORDER_DEFAULT)


    return blur


