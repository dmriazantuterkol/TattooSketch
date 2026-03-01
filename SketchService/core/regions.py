import cv2
import numpy as np

def region_cleanup(image):
    kernel = np.ones((3, 3), np.uint8)
    cleaned = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return cleaned
