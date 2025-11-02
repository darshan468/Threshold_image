import cv2 #importing opencv library

img = cv2.imread("pandya.jpg")   #reading the image
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #converting the image to grayscale
threshold_img = cv2.threshold(grayimg, 150, 255, cv2.THRESH_BINARY)[1]        #applying thresholding on the grayscale image
cv2.imwrite("thresholdpandya.jpg", threshold_img)     #saving the threshold image
cv2.imshow("Threshold Image", threshold_img)   #displaying the threshold image
cv2.waitKey(0)
cv2.destroyAllWindows()