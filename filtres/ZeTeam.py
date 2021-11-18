import cv2

def zeTeam_filter(img):
    title_text = "Philemon Jules Leo"
    title_font = cv2.FONT_HERSHEY_SIMPLEX
    zTf = cv2.putText(img,title_text,(60,350),title_font,1,(255, 140, 234),3)
    return zTf