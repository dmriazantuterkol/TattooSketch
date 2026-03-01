import cv2

def smooth_image(image):
    return cv2.bilateralFilter(image, d=7, sigmaColor=75, sigmaSpace=75)
