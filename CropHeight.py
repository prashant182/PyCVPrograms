import cv2
import numpy as np
import glob
i=0
for cvimg in glob.glob("PATH.png"):
    img=cv2.imread(cvimg)
    height,width=img.shape[:2]
    req_height=2100 #crop the image from bottom 2100 pixels and
    crop_img=img[height-req_height:,:]
    cv2.imwrite('PATH'+'.png',crop_img)
    i=i+1


