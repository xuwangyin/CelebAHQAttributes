import pandas
import os

attr = pandas.read_csv("list_attr_celeba.txt", delim_whitespace=True, header=1)

with open('image_list.txt', 'rt') as file:
	lines = [line.split() for line in file]
	fields = dict()
	for idx, field in enumerate(lines[0]):
		entry_type = int if field.endswith('idx') else str
		fields[field] = [entry_type(line[idx]) for line in lines[1:]]

entries = []	
for i, f in zip(fields['idx'], fields['orig_file']):
	s = attr.loc[f]
	s.name = f'{i+1:05d}.jpg'
	entries.append(s)
df = pandas.DataFrame(entries)
df.to_csv("list_attr_celebahq.txt")
	


