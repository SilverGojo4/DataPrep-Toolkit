import pandas as pd

# 函數: 比較兩個 DataFrame 的每個位置，找出不同之處
def compare_df(df1, df2):
    """ 
    參數: 
    - df1: 第一個要比較的 DataFrame (pandas.DataFrame)
    - df2: 第二個要比較的 DataFrame (pandas.DataFrame)

    返回: 
    - 無
      如果發生錯誤，則返回 None
    """
    try:
        # 檢查兩個 DataFrame 是否有相同的形狀
        if df1.shape != df2.shape:
            print("DataFrames have different shapes")
            return
        
        diff_locations = []  # 用於儲存不同位置的列表

        # 遍歷 DataFrame 的每個元素
        for row in range(df1.shape[0]):
            for col in range(df1.shape[1]):
                if df1.iloc[row, col] != df2.iloc[row, col]:
                    diff_locations.append(((row, col), df1.iloc[row, col], df2.iloc[row, col]))

        # 根據是否有差異，打印相應的信息
        if not diff_locations:
            print("DataFrames are identical")
        else:
            print(f"DataFrames differ at {len(diff_locations)} locations")
            for location, val1, val2 in diff_locations:
                print(f"At location {location}, df1 has value {val1} while df2 has value {val2}")

    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None
