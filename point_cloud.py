#This python script should output a point cloud file generated from the disparity map created by disparity.py
import cv2 as cv
import numpy as np
import open3d as o3d
import os
 
#mutes warning message 
o3d.utility.set_verbosity_level(o3d.utility.VerbosityLevel.Error)

##loads the left image  
color_bgr = cv.imread("data/left.png") #loads the left image
disp16 = np.load("data/disp_raw_int16.npy")       #loads the disparity image
disp = disp16.astype(np.float32) / 16.0           #returns disparity in fixed point format

#converts the disparity to pixels
fx = 700.0      #focal length in pixels 
b  = 0.10       #baseline in meters
disp = cv.medianBlur(disp, 5) 
valid = disp > 0.0 
depth = (fx * b) / np.maximum(disp, 1e-6) 
disp = cv.medianBlur(disp, 5)
print("Created disparity map...", flush=True) 
depth[disp <= 0] = 0

##builds Open3D RGBD and camera intrinsics
h, w = depth.shape #image height and width 
color = cv.cvtColor(color_bgr, cv.COLOR_BGR2RGB) 

rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
    o3d.geometry.Image(color), #builds image
    o3d.geometry.Image(depth.astype(np.float32)),  #meters
    depth_scale=1.0, depth_trunc=4.0, convert_rgb_to_intensity=False
)

intr = o3d.camera.PinholeCameraIntrinsic(
   w, h, fx, fx, w/2 - 0.5, h/2 - 0.5
)

#create, save, and view point cloud
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intr)
print("Created point cloud...", flush=True)
pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])  # flip for Open3D coords
o3d.io.write_point_cloud("point_cloud_open3d.ply",pcd) #open point cloud 
o3d.visualization.draw_geometries([pcd])
#print("[done] wrote point_cloud_open3d.ply")
pcd_close = pcd.scale(3.0, center=pcd.get_center())  #closer version of the figure 
o3d.visualization.O3DVisualizer.show(pcd_close) #close point cloud 

