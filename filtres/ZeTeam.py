import cv2

def zeTeam_filter(img,color):
    """
    applies a filter that writes text on an image
    :param img: base image on which the filter will be applied
    :param color: hexadecimal color
    :return: image with filter applied
    """
    title_text = "Philemon Jules Leo"
    title_font = cv2.FONT_HERSHEY_SIMPLEX
    title_color = color
    zTf = cv2.putText(img,title_text,(60,350),title_font,1,title_color,3)
    return zTf