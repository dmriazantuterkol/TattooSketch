import cv2
from datetime import datetime
from core.pipeline import process
import os

# путь относительно папки SketchService
INPUT = "visualTesting/031.jpg"
OUTPUT_DIR = "visualTesting"

# создаём папку если её нет
os.makedirs(OUTPUT_DIR, exist_ok=True)

# загружаем изображение
img = cv2.imread(INPUT)

if img is None:
    raise FileNotFoundError(f"Не найдено изображение: {INPUT}")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# обработка
result = process(img, colors=6)

# имя файла с временем
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_filename = f"031_result_{timestamp}.png"
output_path = os.path.join(OUTPUT_DIR, output_filename)

# сохраняем
cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))

print("Готово:", output_path)