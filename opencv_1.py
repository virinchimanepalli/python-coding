import imutils
import cv2


image =cv2.imread("pixel.jpg") #To load our image
image1 =cv2.imread("pixel1.jpg")
# imageblock =cv2.imread(args["image"])
(h,w,d) = image.shape#its actually a 
print("height ={} ,width={}, depth={}".format(h,w,d))
(B , G, R)= image[100,50]
print("{},{},{}".format(R ,G ,B))



roi =image[60:160,320:420]
r = 300.0/w
dim = (300, int(h*r))
center = (w//2,h//2)
# resized = cv2.resize(image,dim)
resized = imutils.resize(image, width=300) # Using imutils we can do both 
rotate = imutils.rotate(image,-45)
M = cv2.getRotationMatrix2D(center,-45,1.0)#for Rotating image
rotated = cv2.warpAffine(image, M, (w, h))
bound =imutils.rotate_bound(resized,-45)
blurred =cv2.GaussianBlur(resized,(11,11),0)
output=image1.copy()



cv2.imshow("ROI",roi)
cv2.imshow("opencv rotation",rotated)
cv2.imshow("Aspect ratio resize", resized)
cv2.imshow("using imutils",rotate)
cv2.imshow("bound rotation",bound)
cv2.imshow("smoothing of an image",blurred)
cv2.rectangle(output,(350, 60), (420, 160), (0, 0, 255), 2)
cv2.line(output,(60,20),(400,200),(0,0,255),5)
cv2.imshow("REctangle",output)
cv2.imshow("Line",output)
cv2.waitKey(0)