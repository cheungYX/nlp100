# encoding: UTF-8
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

pattern = re.compile(r'''
    ^       # 行頭
    (={2,}) # キャプチャ対象、2個以上の'='
    \s*     # 余分な0個以上の空白（'哲学'や'婚姻'の前後に余分な空白があるので除去）
    (.+?)   # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
    \s*     # 余分な0個以上の空白
    \1      # 後方参照、1番目のキャプチャ対象と同じ内容
    .*      # 任意の文字が0文字以上
    $       # 行末
	''', re.MULTILINE + re.VERBOSE)

res = pattern.findall(find_uk())

for line in res:
    print(line)