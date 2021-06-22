import json
import codecs

data=json.load(codecs.open('ecg.json', 'r', 'utf-8-sig'))['ecg']['ECG']
for i in data:
    for j in i:
        print(i[j])

