import cv2
from matplotlib import pyplot as plt
imgL = cv2.imread('left_img.jpg',0)
imgR = cv2.imread('right_img.jpg',0)

cv2.imshow('Image', imgL)
#cv2.waitKey(0)
#v2.destroyAllWindows()
stereo = cv2.StereoBM_create(numDisparities=48, blockSize=5)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()