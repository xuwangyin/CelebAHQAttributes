# CelebAHQAttributes"

Extract samples of different genders:

```
from celebahqattr import CelebAHQAttr
dataset = CelebAHQAttr(root='./')
index = dataset.attr_names.index('Male')
for i, (img, attr) in enumerate(dataset):
    if attr[index] == 1:
        img.save(f'CelebAHQGender/Male/{i:05d}.jpg')
    else:
	img.save(f'CelebAHQGender/Female/{i:05d}.jpg')
```

