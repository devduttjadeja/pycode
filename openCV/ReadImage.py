import cv2

img = cv2.imread('./Images/screenshot.JPG',0)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite('./Images/screenshotgray.png',img)
cv2.destroyAllWindows()

