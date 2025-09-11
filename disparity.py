 #This python script should create a disparity map

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

class disparity :

	def __init__(self,showImages):
	#Load the images 
		root = "data" #where images are
 
		#file paths
		imgLeftPath = os.path.join(root,"left.png")
		imgRightPath = os.path.join(root, "right.png") 
		print("[init] loading:", imgLeftPath, "and", imgRightPath) 		

		#reads images from paths and stores them as grayscale for block matching
		self.imgLeft = cv.imread(imgLeftPath, cv.IMREAD_GRAYSCALE)
		self.imgRight = cv.imread(imgRightPath, cv.IMREAD_GRAYSCALE)
		print("[init] shapes:", 
	      		None if self.imgLeft is None else self.imgLeft.shape, 
      	     	 	None if self.imgRight is None else self.imgRight.shape)  # ← ADD THIS
		

		#input checks
		if self.imgLeft is None or self.imgRight is None :
			print("Error: could not load left or right inmage")
			exit()	
		if self.imgLeft.shape != self.imgRight.shape :
			print("Error: left/right images must be the same size")
			exit()

		if showImages :
			plt.figure()  #new figure
			plt.subplot(121)  # subplot grid: 1-row 2-column layout
			plt.imshow(self.imgLeft) #left image
			plt.subplot(122)  #position 2
			plt.imshow(self.imgRight) #right image
			plt.show()

	def computesDepthMapBM(self) :
		print("[BM] computing…") 
		nDispFactor = 6 #multiplier for disparity levels
		#creates a stereoBM object for later computing the disparity map
		#numDisparities = pixel shifts to search (usually multiple of 16)
		#blockSize = size of block window
		stereo = cv.StereoBM.create(numDisparities=16*nDispFactor, blockSize=21)

		#returns diaparity		
		disparity = stereo.compute(self.imgLeft, self.imgRight) 
 
		print("[BM] disparity:", disparity.shape, disparity.dtype,
      "min:", disparity.min(), "max:", disparity.max())  
 
		#shows disparity map in greyscale
		plt.imshow(disparity, 'gray')
		plt.show() 

	def computeDepthMapSGBM(self) :
		print("[SGBM] computing…")
		window_size = 7
		min_disp = 16 #smallest disparity to search
		nDispFactor = 10 #adjust this 
		num_disp = 16*nDispFactor-min_disp
	
		stereo = cv.StereoSGBM_create(minDisparity=min_disp,
						numDisparities=num_disp,
						blockSize=window_size,
						P1 = 8*3*window_size**2,#penalty when disparity diff is 1
						P2 = 32*3*window_size**2,#penalty when dispariy diff is >1
						disp12MaxDiff=1, 
						uniquenessRatio=15,
						speckleWindowSize=0,
						speckleRange=2, #max disparity variation within the specified window
						preFilterCap=63, #truncates values that fall outside range
						mode=cv.STERE_SGBM_MODE_SGBM_3WAY) #most accurate mode

		#calculate disparity map
		disparity = stereo.compute(self.imgLeft, self.imgRight).astype(np.float32) / 16.0

		#display disparity map 
		plt.imshow(disparity, 'gray')
		plt.colorbar()
		plt.show()

if __name__ == "__main__":
    print("[main] running")
     # create the object and preview the input images
    d = disparity(showImages=False)  #dont show the input left and right images

    # run BM
    print("[BM] starting…")
    d.computesDepthMapBM()

    # run SGBM
    print("[SGBM] starting…")
    d.computeDepthMapSGBM()		
	
