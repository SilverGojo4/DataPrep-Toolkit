import nbformat
import pandas as pd

# 函數: 將 DataFrame 中的序列僅保留天然胺基酸
def nature_amino_acid(df):
    """
    參數: 
    - df: 要處理的 DataFrame (pandas.DataFrame)

    返回: 
    - 處理後的 DataFrame (pandas.DataFrame)
      如果發生錯誤，則返回 None
    """
    try:
        nature = list()             # 創建一個空列表來存儲結果
        df['Nature'] = False        # 創建一個新的布林列 'Nature'，用於標記天然胺基酸
        output = False              # 初始化輸出為 False

        # 迭代 DataFrame 中的每個序列  
        for seq in df['Sequence']:

            # 迭代序列中的每個字符
            for char in str(seq): 

                # 檢查字符是否為天然胺基酸中的一個
                if (char == 'R' or char == 'H' or char == 'K' or char == 'D' or char == 'E' or char == 'S' or char == 'T' or char == 'N' or char == 'Q' or char == 'C' or char == 'G' or char == 'P' or char == 'A' or char == 'I' or char == 'L' or char == 'M' or char == 'F' or char == 'W' or char == 'Y' or char == 'V'):
                    output = True   # 如果字符是天然胺基酸，則設置輸出為 True
                else:
                    output = False  # 如果字符不是天然胺基酸，則設置輸出為 False
                    break

            nature.append(output)   # 添加結果到列表中

        df['Nature'] = nature           # 將列表賦值給 'NATURE' 列
        df = df[df['Nature']==True]     # 選擇 'NATURE' 列值為 True 的行，即僅保留天然胺基酸的序列
        
        return df
    
    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None
