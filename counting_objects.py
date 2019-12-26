
# import the necessary packages
import argparse
import imutils
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())
image =cv2.imread(args["image"])
cv2.imshow("image",image)

# convertion of image to gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray,30,150)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts =imutils.grab_contours(cnts)   #cnts is basically counts no. bounded objects
output =image.copy()

mask = thresh.copy()
mask = cv2.erode(mask,None,iterations=5)
cv2.imshow("Erosion",mask)
cv2.waitKey(0)

mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated",mask)
cv2.waitKey(0)

for c in cnts:
	cv2.drawContours(output ,[c],-1,(240,0,159),3)
	cv2.imshow("boundaries",output)
	cv2.waitKey(0) # for loop runs untill every object was bounded

text = " i found {} bounded objects".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)


cv2.imshow("Edged",edged)
cv2.waitKey(0)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.imshow("Thresold",thresh)
cv2.waitKey(0)

