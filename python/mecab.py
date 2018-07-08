#install mecab in mac
# $ pip3 install mecab-python3
# $ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
# $ ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n
#パス確認
# $ echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
# /usr/lib/mecab/dic/mecab-ipadic-neologd
#rcファイル書き換え
# $ sudo nvim /etc/mecabrc 
# dicdir = /usr/lib/mecab/dic/mecab-ipadic-neologd

import MeCab
target_file_name = 'tmp/neko.txt'
result_file_name = 'neko.txt.mecab'

def parse_neko():
    with open(target_file_name) as data_file, \
            open(result_file_name, mode='w') as out_file:

        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))


def neco_lines():
    with open(result_file_name) as file_parsed:

        morphemes = []
        for line in file_parsed:

            # 表層形はtab区切り、それ以外は','区切りでバラす
            cols = line.split('\t')
            if(len(cols) < 2):
                raise StopIteration     # 区切りがなければ終了
            res_cols = cols[1].split(',')

            # 辞書作成、リストに追加
            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            # 品詞細分類1が'句点'なら文の終わりと判定
            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []


# 形態素解析
parse_neko()

# 1文ずつ辞書のリストを作成
lines = neco_lines()
for line in lines:
    print(line)