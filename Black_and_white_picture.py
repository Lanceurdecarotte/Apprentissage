
#importing opencv
import cv2

#charge the picture
img=cv2.imread('AlexHoff.jpg')
#img=cv2.imread('photo_de_classe.webp')

#resize the picture
img_resize= cv2.resize(img,(800,800))

#convert the picture in grey lvls
img_grey=cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

#convert in black and white
img_binary = cv2.threshold(img_grey,128, 255, cv2.THRESH_BINARY)[1]

#display the picture
cv2.imshow('B&W pic',img_binary)

#waiting a keypressed
cv2.waitKey(0)

#faces detection
HaarCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = HaarCascade.detectMultiScale(
   img_grey,
   scaleFactor=1.28,
   minNeighbors=3,
   minSize=(25, 25)
)

#print in terminal the number of faces found
print("INFO : Found {0} Faces!".format(len(faces)))

#loop drawing rectangles on the colored picture
for (x, y, w, h) in faces:
   cv2.rectangle(img_resize, (x, y), (x + w, y + h), (0, 255, 0), 2)

#display the picture
status = cv2.imshow('Faces detected', img_resize)

#waiting a keypressed
cv2.waitKey(0)

#save images
cv2.imwrite('B&W_pic.jpg',img_binary) 
cv2.imwrite('Faces_detected.jpg',img_resize) 
