import cv2
import numpy as np
from sklearn.cluster import KMeans

def posterize(image, k=6):
    h, w, _ = image.shape

    pixels = image.reshape((-1, 3)).astype(np.float32)

    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = kmeans.fit_predict(pixels)

    centers = kmeans.cluster_centers_
    quantized = centers[labels]

    result = quantized.reshape((h, w, 3)).astype(np.uint8)

    return result
