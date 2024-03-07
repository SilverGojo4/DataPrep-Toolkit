import nbformat
from nbformat.v4 import new_code_cell, new_notebook

# 函數: 將 Python 源代碼文件 (.py) 轉換為 Jupyter Notebook (.ipynb)
def py_to_ipynb(py_file_path, ipynb_file_path):
    """
    參數: 
    - py_file_path: Python 源代碼文件的路徑 (str)
    - ipynb_file_path: 要生成的 Jupyter Notebook 的路徑 (str)
    
    返回: 
    - 無
      如果發生錯誤，則返回 None
    """
    try:
        # 從 .py 文件讀取代碼
        with open(py_file_path, 'r') as py_file:
            py_code = py_file.read()

        # 創建一個新的 Jupyter Notebook
        nb = new_notebook()

        # 將 Python 代碼添加到一個新的單元格中
        code_cell = new_code_cell(source=py_code)
        nb.cells.append(code_cell)

        # 將 Notebook 寫入 .ipynb 文件
        with open(ipynb_file_path, 'w') as ipynb_file:
            nbformat.write(nb, ipynb_file)
    
    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the conversion process:\n{e}")
        return None

# 函數: 將 Jupyter Notebook (.ipynb) 轉換為 Python 源代碼文件 (.py)
def ipynb_to_py(ipynb_file_path, py_file_path):
    """
    參數: 
    - ipynb_file_path: Jupyter Notebook 的路徑 (str)
    - py_file_path: 要生成的 Python 源代碼文件的路徑 (str)

    返回: 
    - 無
      如果發生錯誤，則返回 None
    """
    try:
        # 從 .ipynb 文件讀取內容
        with open(ipynb_file_path, 'r') as ipynb_file:
            nb = nbformat.read(ipynb_file, as_version=4)

        # 提取所有代碼單元格
        code_cells = [cell for cell in nb.cells if cell.cell_type == 'code']
        
        # 合併代碼單元格的源代碼
        py_code = '\n\n'.join(cell.source for cell in code_cells)

        # 將代碼寫入 .py 文件
        with open(py_file_path, 'w') as py_file:
            py_file.write(py_code)
    
    except Exception as e:
        # 錯誤處理
        print(f"An error occurred during the conversion process:\n{e}")
        return None

if __name__ == '__main__':
    
    # 請求用戶選擇轉換類型
    choice = input("選擇轉換類型 (1: py 轉 ipynb, 2: ipynb 轉 py): ")
    
    if choice == '1':
        # 執行從 py 轉換為 ipynb
        py_file_path = input("輸入 .py 文件的路徑: ")
        ipynb_file_path = input("輸入輸出 .ipynb 文件的路徑: ")
        py_to_ipynb(py_file_path, ipynb_file_path)

    elif choice == '2':
        # 執行從 ipynb 轉換為 py
        ipynb_file_path = input("輸入 .ipynb 文件的路徑: ")
        py_file_path = input("輸入輸出 .py 文件的路徑: ")
        ipynb_to_py(ipynb_file_path, py_file_path)
    else:
        print("未知選擇！")
