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

def remove_markup(target):

    # 除去対象の正規表現のコンパイル
    pattern = re.compile(r'''
        \'{2,5} # 2〜5個の'
        ''', re.MULTILINE + re.VERBOSE)

    # 空文字に置換
    return pattern.sub('', target)

pattern = re.compile(r'''
    ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
    (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
    ^\}\}$      # '}}'の行
	''', re.MULTILINE + re.VERBOSE + re.DOTALL)

contents = pattern.findall(find_uk())

pattern = re.compile(r'''
    ^\|         # '|'で始まる行
    (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
    \s*         # 空白文字0文字以上
    =
    \s*         # 空白文字0文字以上
    (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
    (?:         # キャプチャ対象外のグループ開始
        (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
    )           # グループ終了
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = pattern.findall(contents[0])

result = {}
keys_test = []
for field in fields:
    result[field[0]] = remove_markup(field[1])
    keys_test.append(field[0])

for item in sorted(result.items(),
        key=lambda field: keys_test.index(field[0])):
    print(item)
