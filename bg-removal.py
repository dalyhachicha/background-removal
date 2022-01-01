import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)
cap.set(3,640) #Width
cap.set(4,480) #Height

segmentor = SelfiSegmentation() #model1 (faster) par default


while True:
    success, img = cap.read()
    img_bg = segmentor.removeBG(img, (255,0,255),threshold=0.8)
    cv2.imshow("Video Feed", img)
    cv2.imshow("Background removed", img_bg)
    cv2.waitKey(1)
