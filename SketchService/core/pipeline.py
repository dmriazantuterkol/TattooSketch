import cv2
import numpy as np

from core.smooth import smooth_image
from core.posterize import posterize
from core.outline import extract_outline
from core.regions import region_cleanup
from core.lighten import lighten_image
from core.comic import comic_flatten

def process(
    image,
    colors=6,
    use_smooth=False,
    use_posterize=False,
    use_region_cleanup=False,
    use_lighten=False,
    use_outline=True,
    use_comic=True,
):
    current = image.copy()

    # 1️⃣ Smooth
    if use_smooth:
        current = smooth_image(current)
        print("✓ smooth")

    # 2️⃣ Comic (Marvel режим)
    if use_comic:
        current = comic_flatten(current, color_levels=colors)
        print("✓ comic")

    # 3️⃣ Posterize (старый режим)
    if use_posterize:
        current = posterize(current, k=colors)
        print("✓ posterize")

    # 4️⃣ Cleanup
    if use_region_cleanup:
        current = region_cleanup(current)
        print("✓ region cleanup")

    # 5️⃣ Lighten
    if use_lighten:
        current = lighten_image(current)
        print("✓ lighten")

    # 6️⃣ Outline
    if use_outline:
        outline = extract_outline(current)
        current[outline > 0] = [0, 0, 0]
        print("✓ outline")

    return current