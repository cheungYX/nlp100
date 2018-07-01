# coding: utf-8
import gzip
import json
import re
tmp_dir = 'tmp/jawiki-country.json.gz'


def find_uk():
    with gzip.open(tmp_dir, 'rt') as data:
        for line in data:
            json_data = json.loads(line)
            if json_data['title'] == 'イギリス':
                return json_data['text']
    raise ValueError('no find')


# 正規表現のコンパイル
pattern = re.compile(r'''
    ^       # 行頭
    .*      # 任意の文字0文字以上
    \[\[Category:
    (       # キャプチャ対象のグループ開始
    .*?     # 任意の文字0文字以上、非貪欲マッチ（貪欲にすると後半の'|'で始まる装飾を巻き込んでしまう）
    )       # グループ終了
    (?:     # キャプチャ対象外のグループ開始
    \|.*    # '|'に続く0文字以上
    )?      # グループ終了、0か1回の出現
    \]\]
    .*      # 任意の文字0文字以上
    $       # 行末
    ''', re.MULTILINE + re.VERBOSE)

# 抽出
result = pattern.findall(find_uk())

# 結果表示
for line in result:
    print(line)