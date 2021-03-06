# nlp100
言語処理100本ノックの問題と答えをここに記す

# Chapter 1: beginning
* 00 [文字列の逆順](./python/reverse.py)
* 01 [パタトクカシーー](./python/patato.py)
* 02 [「パトカー」＋「タクシー」＝「パタトクカシーー」](./python/patoka_taxi.py)
* 03 [円周率](./python/pi.py)
* 04 [元素記号](./python/element.py)
* 05 [n-gram](./python/n-gram.py)
* 06 [集合](./python/union.py)
* 07 [テンプレートによる文生成](./python/temp.py)
* 08 [暗号文](./python/cipher.py)
* 09 [Typoglycemia](./python/random.py)

# Chapter 2: UNIX command
* 10 [行数のカウント](./shell/wc.sh)
* 11 [タブをスペースに置換](./shell/sed.sh)
* 12 [1列目をcol1.txtに，2列目をcol2.txtに保存](./shell/cut.sh)
* 13 [col1.txtとcol2.txtをマージ](./shell/merge.sh)
* 14 [先頭からN行を出力](./shell/head.sh)
* 15 [末尾のN行を出力](./shell/tail.sh)
* 16 [ファイルをN分割する](./shell/split.sh)
* 17 [１列目の文字列の異なり](./shell/diff.sh)
* 18 [各行を3コラム目の数値の降順にソート](./shell/sort.sh)
* 19 [各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる](./shell/count.sh)

# Chapter 3: regular expression
[hightemp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt)は，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

* 20 [JSONデータの読み込み](./python/json_read.py)
* 21 [カテゴリ名を含む行を抽出](./python/category_matcher.py)
* 22 [カテゴリ名の抽出](./python/category_name.py)
* 23 [セクション構造](./python/section.py)
* 24 [ファイル参照の抽出](./python/refer.py)
* 25 [テンプレートの抽出](./python/temp_mather.py)
* 26 [強調マークアップの除去](./python/remove_mark.py)
* 27 [内部リンクの除去](.python/remove_link.py)
* 28 [MediaWikiマークアップの除去](.python/remove_medis.py)
* 29 [国旗画像のURLを取得する](.python/remove_flag_ulr.py)

# Chapter 4: Morphological Analysis
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．

1行に1記事の情報がJSON形式で格納される
各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される

* 30 [形態素解析結果の読み込み](./python/mecab.py)
* 31. 動詞
* 32. 動詞の原形
* 33. サ変名詞
* 34. 「AのB」
* 35. 名詞の連接
* 36. 単語の出現頻度
* 37. 頻度上位10語
* 38. ヒストグラム
* 39. Zipfの法則

# Chapter 5: Dependency analysis
夏目漱石の小説『吾輩は猫である』の文章[neko.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt)をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

* 40. 係り受け解析結果の読み込み（形態素）
* 41. 係り受け解析結果の読み込み（文節・係り受け）
* 42. 係り元と係り先の文節の表示
* 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
* 44. 係り受け木の可視化
* 45. 動詞の格パターンの抽出
* 46. 動詞の格フレーム情報の抽出
* 47. 機能動詞構文のマイニング
* 48. 名詞から根へのパスの抽出
* 49. 名詞間の係り受けパスの抽出

# Chapter 6: English text
英語のテキスト[nlp.txt](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt)に対して，以下の処理を実行せよ．

* 50. 文区切り
* 51. 単語の切り出し
* 52. ステミング
* 53. Tokenization
* 54. 品詞タグ付け
* 55. 固有表現抽出
* 56. 共参照解析
* 57. 係り受け解析
* 58. タプルの抽出
* 59. S式の解析

# Chapter 7: Database
[artist.json.gz](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz)は，オープンな音楽データベース[MusicBrainz](https://musicbrainz.org/)の中で，アーティストに関するものをJSON形式に変換し，gzip形式で圧縮したファイルである．このファイルには，1アーティストに関する情報が1行にJSON形式で格納されている．JSON形式の概要は以下の通りである．
rtist.json.gzのデータをKey-Value-Store (KVS) およびドキュメント志向型データベースに格納・検索することを考える．KVSとしては，LevelDB，Redis，KyotoCabinet等を用いよ．ドキュメント志向型データベースとして，MongoDBを採用したが，CouchDBやRethinkDB等を用いてもよい．

* 60. KVSの構築
* 61. KVSの検索
* 62. KVS内の反復処理
* 63. オブジェクトを値に格納したKVS
* 64. MongoDBの構築
* 65. MongoDBの検索
* 66. 検索件数の取得
* 67. 複数のドキュメントの取得
* 68. ソート
* 69. Webアプリケーションの作成

# Chapter 8: Machine Learning
本章では，Bo Pang氏とLillian Lee氏が公開しているMovie Review Dataのsentence polarity dataset v1.0を用い，文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に分類するタスク（極性分析）に取り組む．

* 70. データの入手・整形
* 71. ストップワード
* 72. 素性抽出
* 73. 学習
* 74. 予測
* 75. 素性の重み
* 76. ラベル付け
* 77. 正解率の計測
* 78. 5分割交差検定
* 79. 適合率-再現率グラフの描画

# Chapter 9: Vector Space Model(1)
[enwiki-20150112-400-r10-105752.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2)は，2015年1月12日時点の英語のWikipedia記事のうち，約400語以上で構成される記事の中から，ランダムに1/10サンプリングした105,752記事のテキストをbzip2形式で圧縮したものである．このテキストをコーパスとして，単語の意味を表すベクトル（分散表現）を学習したい．第9章の前半では，コーパスから作成した単語文脈共起行列に主成分分析を適用し，単語ベクトルを学習する過程を，いくつかの処理に分けて実装する．第9章の後半では，学習で得られた単語ベクトル（300次元）を用い，単語の類似度計算やアナロジー（類推）を行う．

なお，問題83を素直に実装すると，大量（約7GB）の主記憶が必要になる． メモリが不足する場合は，処理を工夫するか，1/100サンプリングのコーパス[enwiki-20150112-400-r100-10576.txt.bz2](http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2)を用いよ．

* 80. コーパスの整形
* 81. 複合語からなる国名への対処
* 82. 文脈の抽出
* 83. 単語／文脈の頻度の計測
* 84. 単語文脈行列の作成
* 85. 主成分分析による次元圧縮
* 86. 単語ベクトルの表示
* 87. 単語の類似度
* 88. 類似度の高い単語10件
* 89. 加法構成性によるアナロジー

# Chapter 10: Vector Space Model(2)
第10章では，前章に引き続き単語ベクトルの学習に取り組む．

* 90. word2vecによる学習
* 91. アナロジーデータの準備
* 92. アナロジーデータへの適用
* 93. アナロジータスクの正解率の計算
* 94. WordSimilarity-353での類似度計算
* 95. WordSimilarity-353での評価
* 96. 国名に関するベクトルの抽出
* 97. k-meansクラスタリング
* 98. Ward法によるクラスタリング
* 99. t-SNEによる可視化
