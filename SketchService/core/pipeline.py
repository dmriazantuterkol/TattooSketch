import cv2
import numpy as np

from core.smooth import smooth_image
from core.posterize import posterize
from core.outline import extract_outline
from core.regions import region_cleanup

def process(image, colors=6):
    smoothed = smooth_image(image)
    poster = posterize(smoothed, k=colors)
    poster = region_cleanup(poster)
    outline = extract_outline(image)

    result = poster.copy()
    result[outline > 0] = [0, 0, 0]

    return result
