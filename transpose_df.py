import pandas as pd

# 函數: 轉置 DataFrame 並保存 CSV
def transpose_df_to_csv(input_file, output_file):
    """
    參數: 
    - input_file: 輸入文件的路徑，指定要讀取和轉置的 CSV 文件 (str)
    - output_file: 輸出文件的路徑，轉置後的 DataFrame 將被保存到這個文件 (str)

    返回: 
    - 轉置後的 DataFrame (pandas.DataFrame)
      如果發生錯誤，則返回 None
    """
    
    try:
        # 讀取文件
        df = pd.read_csv(filepath_or_buffer=input_file)

        # 獲取原始第一列的列名
        original_first_column_name = df.columns[0]
        
        # 將第一列設為索引並轉置 DataFrame
        df.set_index(df.columns[0], inplace=True)
        df = df.T

        # 轉置 DataFrame 並保存 CSV，保留索引
        df.to_csv(path_or_buf=output_file, index=True)

        # 重新讀取保存的文件，移除索引，再次保存
        df = pd.read_csv(filepath_or_buffer=output_file)

        # 重命名第一列為 'id'
        df.rename(columns={df.columns[0]: original_first_column_name}, inplace=True)
        
        df.to_csv(path_or_buf=output_file, index=False)

        # 最後再次讀取並返回 DataFrame
        df = pd.read_csv(filepath_or_buffer=output_file)

        return df

    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None
