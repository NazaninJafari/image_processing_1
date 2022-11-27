import cv2
import numpy as np

images = [[0 for i in range(5)] for j in range(4)]

for i in range(4):
    for j in range(5):
        images[i][j] = cv2.imread(f"{(i+1)}/{j}.jpg", 0)

result = [0 for i in range(4)]

#remouve the noise
for i in range(4):
    for j in range(5):
        result[i] += (images[i][j] /5)

#rows and col of final_pic => rows and cols of images *2 => 1000*2=2000
finale_pic = np.zeros((2000,2000), np.uint8)

finale_pic[0:1000, 0:1000]= result[0]
finale_pic[0:1000, 1000:2000]= result[1]
finale_pic[1000:2000, 0:1000]= result[2]
finale_pic[1000:2000, 1000:2000]= result[3]

cv2.imwrite('result.jpg', finale_pic)
cv2.imshow('new pic', finale_pic)
cv2.waitKey()