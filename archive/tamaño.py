import os
import numpy as np
from collections import Counter
from PIL import Image

root = r"C:\Users\Usuario\Downloads\archive\images"
jpgs = [f for f in os.listdir(root) if f.lower().endswith(".jpg")]

anchos, altos, modos, corruptas = [], [], Counter(), []
for f in jpgs:
    try:
        with Image.open(os.path.join(root, f)) as img:
            anchos.append(img.width)
            altos.append(img.height)
            modos[img.mode] += 1
    except Exception:
        corruptas.append(f)

anchos, altos = np.array(anchos), np.array(altos)
print("Imágenes leídas:", len(anchos), "| Corruptas:", len(corruptas), corruptas[:5])
print("Modos de color:", dict(modos))
print(f"Ancho  -> min {anchos.min()}, max {anchos.max()}, media {anchos.mean():.0f}, mediana {np.median(anchos):.0f}")
print(f"Alto   -> min {altos.min()}, max {altos.max()}, media {altos.mean():.0f}, mediana {np.median(altos):.0f}")
print("Tamaños distintos:", len(set(zip(anchos, altos))))
print("Más comunes:", Counter(zip(anchos.tolist(), altos.tolist())).most_common(5))
print("Imágenes con lado menor a 128 px:", int((np.minimum(anchos, altos) < 128).sum()))