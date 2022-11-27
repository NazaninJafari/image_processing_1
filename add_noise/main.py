import cv2
import random

def sp_noise(img):
    
    h,w = img.shape[0] ,img.shape[1]
    for i in range(0,100):
        rdni = random.randint(0, h)
        rdnj = random.randint(0, w)
        if img[rdni][rdnj] <= 150:
            img[rdni][rdnj] = 255
        else:
            img[rdni][rdnj] = 0

    return img

image = cv2.imread('picture1.jpg', 0)
image_noise = sp_noise(image)
cv2.imwrite('output.jpg', image_noise)
cv2.imshow('pic' , image_noise)
cv2.waitKey()                        