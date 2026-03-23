import cv2
import numpy as np


def extract_outline(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # --- 1. обычные edges
    edges_canny = cv2.Canny(gray, 120, 240)

    # --- 2. границы цветовых зон (🔥 ключ)
    diff = np.zeros_like(gray)

    diff |= (gray != np.roll(gray, 1, axis=0))
    diff |= (gray != np.roll(gray, -1, axis=0))
    diff |= (gray != np.roll(gray, 1, axis=1))
    diff |= (gray != np.roll(gray, -1, axis=1))

    edges_regions = (diff > 0).astype(np.uint8) * 255

    # --- 3. объединяем
    edges = edges_regions.copy()

# добавляем canny только где нет регионов
    edges[(edges == 0) & (edges_canny > 0)] = 255
    # --- 4. чистка
    kernel = np.ones((2, 2), np.uint8)
   #  edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
   # --- thinning (делает линии тонкими)
    try:
        edges = cv2.ximgproc.thinning(edges)
    except:
        pass
    
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(edges, connectivity=8)

    clean = np.zeros_like(edges)

    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]

        if area >40:  # 🔥 главный параметр
            clean[labels == i] = 255

    edges = clean

    return edges