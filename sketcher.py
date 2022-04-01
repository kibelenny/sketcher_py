#Photo Sketching Using Python
import cv2
import os

path = input('Enter Image Path: ')
img = cv2.imread(path)

#Convert to Gray
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255-gray_image

#Blurring The Inverted Gray Image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (19,19),0)
inverted_blurred_image = 255-blurred_image

#Sketching
sketched = cv2.divide(gray_image, inverted_blurred_image,scale= 256.0)

#Path for exporting image
dir = os.path.dirname(path)
name = os.path.basename(path)
new_name = name.split('.')[0] + '_sketched' + '.' + name.split('.')[-1]
new_path = os.path.join(dir, new_name)

#Export Image
cv2.imwrite(new_path,sketched)