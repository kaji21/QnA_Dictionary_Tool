import sys
import mecab_util
import csv_util

args = sys.argv
input_file_path = args[1]
tansi_dic_file_path = args[2]

# inputのFileオープン
with open(input_file_path, encoding='utf-8') as f:
    faq = f.read()

# inputのFileから質問本文と回答本文を抽出

# 質問本文と回答本文をmecabで形態素解析する
mecabed_faq = mecab_util.mecab_list(faq)
csv_util.csv_wirter(mecabed_faq, 'mecabed_faq.csv')

# 形態素解析した結果、行をマージして重複を無くす
merged_faq = mecab_util.mecab_merge(mecabed_faq)
csv_util.csv_wirter(merged_faq, 'merged_faq.csv')

# 「たんし」を開き、マージした行と一致する「表記ゆれと見なされる単語群」を抽出する
# 「たんし」で「表記ゆれと見なされる単語群」を追加したファイルを出力する
faq_added_tansi = mecab_util.tansi_merge(merged_faq, tansi_dic_file_path)
csv_util.csv_wirter(faq_added_tansi, 'faq_added_tansi.csv')

# json整形

