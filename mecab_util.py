import MeCab
import sys
import csv

# 質問本文と回答本文をmecabで形態素解析
def mecab_list(text):
    tagger = MeCab.Tagger("-Ochasen")
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_class = []
    while node:
        word = node.surface
        wclass = node.feature.split(',')
        if wclass[0] != u'BOS/EOS':
            if wclass[6] == None:
                word_class.append((word,wclass[0],wclass[1],wclass[2],""))
            else:
                word_class.append((word,wclass[0],wclass[1],wclass[2],wclass[6]))
        node = node.next
    return word_class

# 形態素解析した結果、行をマージして重複を無くす。
def mecab_merge(target_text):
    merged_text = []
    for target_line in target_text:
        for merged_line in merged_text:
        # 条件がおかしいかも。。。
        # 活用形が*のときは、もとの語が一致するかも確認
            if merged_line[4] == '*' and target_line[0] == merged_line[0]:
                break
            elif target_line[4] == merged_line[4] and target_line[0] == merged_line[0]:
                break
        else:
            merged_text.append(target_line)
    return merged_text

# 「たんし」を開き、マージした行と一致する「表記ゆれと見なされる単語群」を抽出する
def tansi_merge(target_text, tansi_path):
    merged_text = []
    for target_line in target_text:
        with open(tansi_path, encoding='utf-8') as f:
            tansi_dic = csv.reader(f, delimiter='\t')
            for tansi_line in tansi_dic:
                # 条件が適当。。。
                if target_line[4] == '*' and target_line[0] == tansi_line[0]:
                    target_line_add_tansi = target_line + (tansi_line[5],)
                    merged_text.append(target_line_add_tansi)
                    break
                elif target_line[4] == tansi_line[0]:
                    target_line_add_tansi = target_line + (tansi_line[5],)
                    merged_text.append(target_line_add_tansi)
                    break
            else:
                target_line_add_tansi = target_line + ('',)
                merged_text.append(target_line_add_tansi)
    return merged_text