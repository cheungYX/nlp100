#!/bin/sh
# sedのsコマンド： s/検索パターン/置換文字列/g（すべて置換）
sed 's/\t/ /g' tmp/hightemp.txt

# trコマンド 
#tr '\t' ' ' < tmp/hightemp.txt

# expandコマンド
#expand --tabs=1 tmp/hightemp.txt
