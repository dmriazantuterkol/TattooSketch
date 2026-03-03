import cv2
import numpy as np


def extract_outline(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 120, 240)
    return edges