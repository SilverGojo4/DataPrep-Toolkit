import pandas as pd

# 函數: 將序列長度限制在下界到上界之間
def seq_length_cut(df, lower_bound, upper_bound):
    """
    參數: 
    - df: 要處理的 DataFrame (pandas.DataFrame)
    - lower_bound: 序列長度的下界 (int)
    - upper_bound: 序列長度的上界 (int)

    返回: 
    - 處理後的 DataFrame (pandas.DataFrame)
      如果發生錯誤，則返回 None
    """
    try:
        # 確保輸入是 DataFrame
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")

        # 檢查上界是否大於下界
        if lower_bound >= upper_bound:
            raise ValueError("Lower bound must be less than upper bound")

        # 介於 lower_bound ~ upper_bound 之間的行
        df = df[df['Sequence_Length'] > lower_bound]  # 選擇序列長度大於 lower_bound 的行
        df = df[df['Sequence_Length'] < upper_bound]  # 選擇序列長度小於 upper_bound 的行
        
        return df
    
    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None
