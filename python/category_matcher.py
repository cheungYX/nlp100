import json
import gzip
import re
tmp_dir = "tmp/jawiki-country.json.gz"

def find_uk():
    with gzip.open(tmp_dir, 'rt') as data:
        for line in data:
            json_data = json.loads(line)
            if json_data['title'] == 'イギリス':
                return json_data['text']
    raise ValueError('no find')

pattern = '^(.*\[\[Category:.* \]\].*)$'
res = re.findall(pattern, find_uk())

for line in res:
    print(line)