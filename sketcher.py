#Photo Sketching Using Python
import cv2
import os

path = input('Enter Image Path: ')
img = cv2.imread(path)

#Resize Image.
sizes = [128,256,360,480,512,720,800]
for size in sizes:
    aspect_ratio = img.shape[1]/size
    new_width = int(img.shape[1]/aspect_ratio)
    new_height = int(img.shape[0]/aspect_ratio)
    dims = (new_width, new_height)
    print(dims)
    img_resized = cv2.resize(img, dims, interpolation=cv2.INTER_AREA)

    #Convert to Gray
    gray_image = cv2.cvtColor(img_resized,cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255-gray_image

    #Blurring The Inverted Gray Image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (19,19),0)
    inverted_blurred_image = 255-blurred_image

    #Sketching
    sketched = cv2.divide(gray_image, inverted_blurred_image,scale= 256.0)

    #Path for exporting image
    #dir = os.path.dirname(path)
    dir = r'C:\users\lenny\desktop\outs'
    name = os.path.basename(path)
    new_name = name.split('.')[0] + '_ss' + '.' + name.split('.')[-1]
    new_path = os.path.join(dir, new_name)
    

    #Export Image
    cv2.imwrite(new_path,sketched)