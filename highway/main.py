from email.mime import image
import cv2
import numpy as np

images= []
for i in range(0,15):
    img = cv2.imread(f'h{i}.jpg', 0)
    images.append(img)
    h, w = img.shape

result = np.zeros((h,w) , np.uint8)
for img in images:
    result += img// 15

cv2.imwrite('vid_highway.jpg', result)
cv2.imshow('highway', result)
cv2.waitKey()
