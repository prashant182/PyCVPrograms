import cv2
import numpy as np
import glob

def trim(frame):
    #crop top
    if not np.sum(frame[1]):
        return trim(frame[2:])
    #crop bottom
    elif not np.sum(frame[-2]):
        return trim(frame[:-3])
    #crop left
    elif not np.sum(frame[:,1]):
        return trim(frame[:,2:])
    #crop right
    elif not np.sum(frame[:,-2]):
        return trim(frame[:,:-3])
    return frame

i=0;
for cvimg in glob.glob("PATH/.jpg"):
    img=cv2.imread(cvimg)
    thold = (img > 120) * img
    trimmedimage = trim(thold)
    cv2.imwrite('PATH'+str(i)+'.jpg', trimmedimage)
    i=i+1



