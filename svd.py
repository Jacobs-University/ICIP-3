import numpy as np
import cv2
from skimage import color


def svdbd(image, numofsv):
    # image is already a array
    image = color.rgb2gray(image)
    u,s,v = np.linalg.svd(image)
    tsv = np.sum(s[0:numofsv])
    sumsv = np.sum(s)
    out = tsv/sumsv
    return out
    
    