# encoding: UTF-8
import json
import gzip
tmp_dir = "tmp/jawiki-country.json.gz"

with gzip.open(tmp_dir, 'rt') as data:
    for line in data:
        json_data = json.loads(line)
        if json_data['title'] == 'イギリス':
            print(json_data['text'])
            break