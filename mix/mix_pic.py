from ctypes.wintypes import RGB
import cv2
import numpy as np

img1 = cv2.imread('nazanin.jpg', 0)
img2 = cv2.imread('neslihan_arslan.jpg', 0)


height, width, depth= min(img1.shape[0],img2.shape[0]), min(img1.shape[1],img2.shape[1]), 3

#resizing images
img2_resized = cv2.resize(img2, (width,height))
img1_resized = cv2.resize(img1, (width,height))

alpha= 0.5
beta= 0.5
blend_image1 = cv2.addWeighted(img1_resized, alpha, img2_resized, beta, gamma=0)

alpha = 1
blend_image2 = cv2.addWeighted(img1_resized, alpha, img2_resized, beta, gamma=0)

new_width= width*4
final_pic = np.zeros((height,new_width), dtype='uint8')

#final_pic = cv2.hconcat([img1_resized, blend_image1, blend_image2, img2_resized])
final_pic[0:height, 0:width] = img1_resized
final_pic[0:height, width:2*width] = blend_image2
final_pic[0:height, 2*width:3*width] = blend_image1
final_pic[0:height, 3*width:4*width] = img2_resized

cv2.imwrite('output.jpg', final_pic)
cv2.imshow('output' , final_pic)
cv2.waitKey()