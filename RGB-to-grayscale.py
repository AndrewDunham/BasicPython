import numpy as np
import cv2
import math


img = cv2.imread('Gudhal.png',1)
height,width,chan = img.shape
print(width,height)
img_bl = np.empty((height,width), dtype=np.uint8)

img_bl=(img[:, :, 0]+img[ :, :, 1]+img[:, :, 2])/3

cv2.imwrite("greyscale.png", img_bl)              


