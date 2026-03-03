import cv2
import numpy as np


def comic_flatten(image, color_levels=6):
    """
    Comic mode v2
    Больше деталей, меньше агрессивного сглаживания.
    """

    # 1️⃣ лёгкое сглаживание
    smoothed = cv2.bilateralFilter(image, d=5, sigmaColor=40, sigmaSpace=40)

    # 2️⃣ перевод в LAB для работы со светлотой
    lab = cv2.cvtColor(smoothed, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)

    # 3️⃣ квантование ТОЛЬКО светлоты
    step = 256 // color_levels
    l = (l // step) * step

    lab_quant = cv2.merge((l, a, b))
    result = cv2.cvtColor(lab_quant, cv2.COLOR_LAB2RGB)

    # 4️⃣ лёгкое повышение резкости (чтобы вернуть детали)
    blurred = cv2.GaussianBlur(result, (0, 0), 1.0)
    result = cv2.addWeighted(result, 1.3, blurred, -0.3, 0)

    return result