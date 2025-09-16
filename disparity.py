#This python script should create a disparity map

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np 

#load the images
imgL = cv.imread('data/left.png',0)
imgR = cv.imread('data/right.png',0) 

#input validation
if imgL is None or imgR is None:
        raise FileNotFoundError("Could not load data/left.png or data/right.png")
if imgL.shape != imgR.shape:
        raise ValueError("Left and right images must have the same shape")

#SGBM Parameters
block = 7    #window size
min_disp = 0 #minimum disparity to search
num_disp = 16 * 10         #search range,must be a multiple of 16

#SGBM matcher
stereo = cv.StereoSGBM_create(
    minDisparity=min_disp,
    numDisparities=num_disp,
    blockSize=block,
    P1=8 * block ** 2,   # smoothness penalty (P1)
    P2=32 * block ** 2,  # smoothness penalty (P2 > P1)
    disp12MaxDiff=1, #left to right consistency check 
    uniquenessRatio=10,
    speckleWindowSize=50,
    speckleRange=2,
)

#calculate disparity 
disparity = stereo.compute(imgL, imgR)

#save disparity for point cloud
np.save("data/disp_raw_int16.npy", disparity)

#show images ('jet' colormap)
plt.subplot(1,3,1), plt.imshow(imgL, 'gray')
plt.xticks([]), plt.yticks([]),plt.title('Left Image')

plt.subplot(1,3,2),plt.imshow(imgR, 'gray')
plt.xticks([]),plt.yticks([]),plt.title('Right Image')

plt.subplot(1,3,3),plt.imshow(disparity, 'jet')
plt.xticks([]),plt.yticks([]), plt.title('Disparity Image')

plt.show()

