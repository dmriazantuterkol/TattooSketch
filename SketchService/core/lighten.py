import cv2
import numpy as np


def lighten_image(image, brightness=25, saturation_scale=0.8):
    """
    Делает изображение светлее и менее насыщенным.
    Используется как подложка под контур.
    """

    # переводим в HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV).astype(np.float32)

    # увеличиваем яркость (V)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] + brightness, 0, 255)

    # уменьшаем насыщенность (S)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation_scale, 0, 255)

    hsv = hsv.astype(np.uint8)

    # обратно в RGB
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

    return result