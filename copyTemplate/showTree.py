import os
import shutil
from pathlib import Path

# https://kknews.cc/zh-tw/code/8vyp8pn.html
#


# 展示目錄樹
# 下一個示例定義了一個函數tree()，該函數的作用是列印一個表示文件層次結構的可視樹，該樹以一個給定目錄為根。
# 因為想列出其子目錄，所以我們要使用.rglob()方法：
# def tree(directory):
#     print(f'+{directory}')
#     for path in sorted(directory.rglob('*')):
#         depth = len(path.relative_to(directory).parts)
#         spacer = ' ' * depth
#         print(f'{spacer}+ {path.name}')

rootDir = "c:\Temp"
tempEmpty = "SAB-空白"

p = Path(rootDir)
srcDir = p / tempEmpty

if srcDir.exists() & srcDir.is_dir():
    print(srcDir)
     # tree(srcDir)
else:
    print(srcDir, "not exist")


print(srcDir.parts, type(srcDir.parts))
for path in sorted(srcDir.iterdir()):
    print(path, type(path))


# 資料夾複製
# shutil.copytree()

# 檔案複製
# shutil.copy(source, destination)


# 永久刪除檔案

# 永久刪除資料夾

# 安全刪除

# 走訪目錄樹

# 使用zipfile 模組壓縮檔案

# 讀取zip檔案

# 從zip檔解壓縮

# 建立和新增到zip檔案中

# 日期格式

# 檔案更名

# 比對檔名中的日期格式

