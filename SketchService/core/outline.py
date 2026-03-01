import cv2
import numpy as np

def extract_outline(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 80, 160)
    edges = cv2.dilate(edges, np.ones((2, 2), np.uint8), iterations=1)
    return edges
