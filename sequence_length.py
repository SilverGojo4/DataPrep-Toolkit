import pandas as pd

# 函數: 計算每個序列的長度並添加到 DataFrame 中
def seq_length(df):
    """
    參數: 
    - df: 要處理的 DataFrame (pandas.DataFrame)

    返回: 
    - 處理後的 DataFrame (pandas.DataFrame)
      如果發生錯誤，則返回 None
    """
    try:
        # 確保輸入是 DataFrame
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")

        # 計算每個長度
        df['Sequence_Length'] = df['Sequence'].apply(len)
        return df
    
    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None
