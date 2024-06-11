import cv2
import pywhatkit as kit

kit.text_to_handwriting("Meet my baby dragon, everyone!", "handwriting.jpg")
img = cv2.imread("handwriting.jpg")
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
