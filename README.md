# CelebAHQAttributes"

Extract samples of different genders:

```
import pathlib
from PIL import Image
from celebahqattr512 import CelebAHQAttr
dataset = CelebAHQAttr(root='./')
target_attr = 'Male'
pathlib.Path(f'{target_attr}1/data').mkdir(parents=True, exist_ok=True)
pathlib.Path(f'{target_attr}0/data').mkdir(parents=True, exist_ok=True)
index = dataset.attr_names.index(target_attr)
for i, (img, attr) in enumerate(dataset):
    img = img.resize([256, 256], Image.LANCZOS)
    if attr[index] == 1:
        img.save(f'{target_attr}1/data/{i:05d}.png')
    else:
        img.save(f'{target_attr}0/data/{i:05d}.png')
```
