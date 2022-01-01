import cv2
import cvzone

from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)
cap.set(3,640) #Width
cap.set(4,480) #Height

#Background image path
bg_img_path = r"C:\\Users\\Daly\\Desktop\\Background removal\\source code\\bg-imgs\\1.jpg" 

img_bg = cv2.imread(bg_img_path)

segmentor = SelfiSegmentation() #model1 (faster/landscape) DEFAULT


while True:
    success, img = cap.read()
    img2 = segmentor.removeBG(img, imgBg=img_bg,threshold=0.8)
    img_stack = cvzone.stackImages([img,img2],2,1)
    cv2.imshow("Video Background removal", img_stack)


    k = cv2.waitKey(33)
    if k==27:  # Esc key to stop
        break
