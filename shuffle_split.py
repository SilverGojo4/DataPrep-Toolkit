from sklearn.model_selection import train_test_split
import pandas as pd

# 函數: 打亂數據集並分割為訓練集和測試集，然後分別保存到指定的路徑
def shuffle_split_to_csv(df, train_output_file, test_output_file, test_size=0.2, random_state=42):
    """
    參數: 
    - df: 要處理的 DataFrame (pandas.DataFrame)
    - train_output_file: 訓練集的輸出路徑 (str)
    - test_output_file: 測試集的輸出路徑 (str)
    - test_size: 測試集佔總數據集的比例 (float, 預設為 0.2)
    - random_state: 隨機種子 (int, 預設為 42)

    返回: 
    - 訓練集和測試集的 DataFrame (pandas.DataFrame)
      如果發生錯誤，則返回 None, None
    """

    try:
        # 打亂數據
        df_shuffled = df.sample(frac=1, random_state=random_state)

        # 分割為訓練集和測試集
        train_df, test_df = train_test_split(df_shuffled, test_size=test_size, random_state=random_state)

        # 保存訓練集和測試集到 CSV 文件
        train_df.to_csv(path_or_buf=train_output_file, index=False)
        test_df.to_csv(path_or_buf=test_output_file, index=False)

        return train_df, test_df

    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None, None
