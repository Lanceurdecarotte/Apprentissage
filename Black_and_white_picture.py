
#importing opencv
import cv2

#charge the picture with grey lvls
img=cv2.imread('AlexHoff.jpg',0)

#convert in black and white
img_binary = cv2.threshold(img,128, 255, cv2.THRESH_BINARY)[1]

#resize the picture
img_resize= cv2.resize(img_binary,(800,800))

#display the picture
cv2.imshow('image',img_resize)

#waiting a keypressed
cv2.waitKey(0)

#save image
cv2.imwrite('AlexHoff2.jpg',img_resize) 