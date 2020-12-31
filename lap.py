import cv2
import numpy as np
import math

# Laplacian functiomn
def laplacian(image):
    out = cv2.Laplacian(image, cv2.CV_64F).var()
    return out


