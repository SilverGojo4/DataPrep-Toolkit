import numpy as np
import pandas as pd

# 函數: 計算每個序列的原子重量並添加到 DataFrame 中
def Cal_weight(df):
    """
    參數: 
    - df: 要處理的 DataFrame (pandas.DataFrame)

    返回: 
    - 處理後的 DataFrame (pandas.DataFrame)
      如果發生錯誤，則返回 None
    """
    try:
        # 計算原子重量
        weights = {'A': 71.08, 'C': 103.15, 'D': 115.09, 'E': 129.12, 'F': 147.18, 
                   'G': 57.05, 'H': 137.14, 'I': 113.16, 'K': 128.18, 'L': 113.16, 
                   'M': 131.20, 'N': 114.11, 'P': 97.12, 'Q': 128.13, 'R': 156.19, 
                   'S': 87.08, 'T': 101.11, 'V': 99.13, 'W': 186.22, 'Y': 163.18 }

        df['Atomic_Mass']= df['Sequence'].map(lambda seq: sum(weights[p] for p in seq))
        
        return df

    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None
