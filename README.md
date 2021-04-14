# CelebAHQAttributes"

Extract samples of different genders:

```
from celebahqattr import CelebAHQAttr
dataset = CelebAHQAttr(root='./')
target_attr = 'Male'
index = dataset.attr_names.index(target_attr)
for i, (img, attr) in enumerate(dataset):
    if attr[index] == 1:
        img.save(f'{target_attr}1/{i:05d}.jpg')
    else:
	img.save(f'{target_attr}0/{i:05d}.jpg')
```
