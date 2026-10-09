import os, re
from collections import Counter
from PIL import Image

root = r"C:\Users\Usuario\Downloads\archive\images"

jpgs = [f for f in os.listdir(root) if f.lower().endswith(".jpg")]
otros = [f for f in os.listdir(root) if not f.lower().endswith(".jpg")]
print("JPG:", len(jpgs), "| Otros:", otros)

clases = Counter(re.sub(r"_\d+\.jpg$", "", f, flags=re.I) for f in jpgs)
print("Número de clases:", len(clases))
for c, n in sorted(clases.items()):
    print(f"{c:28s} {n:4d}  {'gato' if c[0].isupper() else 'perro'}")

corruptas, tamanos, modos = [], Counter(), Counter()
for f in jpgs:
    try:
        with Image.open(os.path.join(root, f)) as img:
            img.verify()
        with Image.open(os.path.join(root, f)) as img:
            tamanos[img.size] += 1
            modos[img.mode] += 1
    except Exception:
        corruptas.append(f)

print("Corruptas:", len(corruptas), corruptas[:5])
print("Modos de color:", dict(modos))
print("Tamaños distintos:", len(tamanos), "| más comunes:", tamanos.most_common(3))