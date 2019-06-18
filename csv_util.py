import sys
import pandas as pd

def csv_wirter(target_text, file_name):
    print(len(target_text))
    df = pd.DataFrame(target_text)
    df.to_csv(file_name, index=None, encoding='utf-8')
