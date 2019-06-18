## 形態素

### AnacondaとMeCabのインストール
https://qiita.com/sta/items/6d29da0dc7069ffaae60

```mecabのパス通す
set "PATH=C:\Program Files\MeCab\bin;%PATH%"
python -c "import os; print('\n'.join(os.environ['PATH'].split(';')))"
```

### MeCabを使う
https://qiita.com/menon/items/2b5ad487a98882289567

```python
import MeCab

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
```

### NEologd辞書をインストール
https://qiita.com/zincjp/items/c61c441426b9482b5a48

か

https://www.pytry3g.com/entry/MeCab-NEologd-Windows


### conda関連
<https://qiita.com/Atupon0302/items/ee3303629ce0b2ae58d7>
```
conda create -n py37 python=3.7
conda activate py37
conda info -e
conda install -n py37 numpy
conda install -n py37 pandas
conda list -n py37
```