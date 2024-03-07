import pandas as pd

# 函數: FASTA 檔案轉換成 DataFrame
def fasta_to_dataframe(fasta_file):
    """
    參數: 
    - fasta_file: FASTA 檔案的路徑，指定要讀取並轉換的 FASTA 文件 (str)

    返回: 
    - 包含序列名稱 (Name) 和序列 (Sequence) 的 DataFrame (pandas.DataFrame)
      如果發生錯誤，則返回 None
    """
    try:
        names = []          # 用於存儲序列名稱的列表
        sequences = []      # 用於存儲序列的列表
        
        with open(fasta_file, 'r') as file:

            sequence = '' # 初始化序列變數

            for line in file:
                if line.startswith('>'):            # 識別標題行
                    if sequence:                    # 如果已存在序列，則將其添加到列表中
                        sequences.append(sequence)
                        sequence = ''               # 重置序列變數
                    names.append(line[1:].strip())  # 添加新的標題 (去除 '>')

                else:  
                    sequence += line.strip()        # 序列行
                    
            if sequence:
                sequences.append(sequence)          # 確保在文件末尾添加最後一個序列 (如果非空)

        # 創建 DataFrame
        df = pd.DataFrame({
            'Name': names,
            'Sequence': sequences
        })
        
        return df
    
    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the process:\n{e}")
        return None
