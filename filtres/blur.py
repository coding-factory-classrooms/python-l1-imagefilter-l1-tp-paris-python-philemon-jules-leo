import cv2

def blur_filter(img,pow):
    fimage = cv2.imread(img)
    blur = cv2.GaussianBlur(fimage, (pow,pow),cv2.BORDER_DEFAULT)


    return blur


    # cv2.imwrite("jhgf.jpg", blur)