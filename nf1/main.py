import cv2
import numpy as np

imga = cv2.imread('a.tif' , 0)
imgb = cv2.imread('b.tif', 0)

result = np.zeros((imga.shape[0], imga.shape[1]), np.uint8)

for i in range(imga.shape[0]):
    for j in range(imga.shape[1]):
        result[i][j] = imga[i][j] - imgb[i][j] + 255

cv2.imwrite('new_img.tif', result)
cv2.imshow('result', result)
cv2.waitKey()