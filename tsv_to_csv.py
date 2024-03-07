import csv

# 函數: 將 .tsv 文件轉換為 .csv 文件
def tsv_to_csv(input_file, output_file):
    """
    參數: 
    - input_file: 要轉換的 .tsv 文件的路徑 (str)
    - output_file: 轉換後生成的 .csv 文件的路徑 (str)

    返回: 
    - 無
      如果發生錯誤，則返回 None
    """
    
    try:
        # 打開 .tsv 文件並讀取內容
        with open(input_file, 'r') as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter='\t')
            
            # 打開或創建 .csv 文件，準備寫入轉換後的內容
            with open(output_file, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                
                # 逐行讀取 .tsv 文件並寫入 .csv 文件
                for row in tsv_reader:
                    csv_writer.writerow(row)

    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the conversion process:\n{e}")

if __name__ == '__main__':
    
    # 請求用戶輸入 .tsv 文件和目標 .csv 文件的路徑
    input_file = input("輸入 .tsv 文件的路徑: ")
    output_file = input("輸入輸出 .csv 文件的路徑: ")
    
    # 執行轉換函數
    tsv_to_csv(input_file, output_file)
