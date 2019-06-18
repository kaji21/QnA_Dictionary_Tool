import sys
import pandas as pd
import mecab_list

args = sys.argv
input_file_path = args[1]

# inputのFileオープン
with open(input_file_path, encoding='utf-8') as f:
    faq = f.read()

# inputのFileから質問本文と回答本文を抽出

# 質問本文と回答本文をmecabで形態素解析
mecab_result = mecab_list.mecab_list(faq)
print(len(mecab_result))
df = pd.DataFrame(mecab_result)
df.to_csv('mecab_result.csv', index=None, encoding='utf-8')

# 形態素解析した結果、行をマージして重複を無くす。
mecab_result_merged = []
for mecab_result_sentence in mecab_result:
    for sentence_merged in mecab_result_merged:
        # ロジックがおかしいかも。。。
        # 活用形が*のときは、もとの語が一致するかも確認
        if sentence_merged[4] == '*' and mecab_result_sentence[0] == sentence_merged[0]:
            break
        elif mecab_result_sentence[4] == sentence_merged[4] and mecab_result_sentence[0] == sentence_merged[0]:
            break
    else:
        mecab_result_merged.append(mecab_result_sentence)

# マージした結果をFileに出力する。
print(len(mecab_result_merged))
df = pd.DataFrame(mecab_result_merged)
df.to_csv('mecab_result_merged.csv', index=None, encoding='utf-8')
