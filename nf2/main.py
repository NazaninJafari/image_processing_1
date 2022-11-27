import cv2

org = cv2.imread('board - origin.bmp', 0)
tst = cv2.imread('board - test.bmp', 0)

img_org = cv2.resize(org, (400,500))
img_tst = cv2.resize(tst, (400,500))

flip_img_tst = cv2.flip(img_tst, 1)
result = cv2.subtract(img_org , flip_img_tst)

cv2.imwrite('result.jpg', result)
cv2.imshow('new pic', result)
cv2.waitKey()