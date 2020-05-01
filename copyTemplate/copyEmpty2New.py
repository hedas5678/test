import shutil
from pathlib import Path
from xml.dom.minidom import parse
import xml.dom.minidom

# Python3 XML 解析
# https://docs.python.org/3/library/xml.dom.html
# https://www.runoob.com/python3/python3-xml-processing.html
# https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/370194/
# https://www.1ju.org/python/python-xml-processing
# https://www.runoob.com/python/python-xml.html
#
# pathlib 教學
# https://kknews.cc/zh-tw/code/8vyp8pn.html
# http://c.biancheng.net/view/2541.html
#

# 目錄複製
def copydirs(srcdir, destdir):
    if srcdir.exists() & (not destdir.exists()):
        if srcdir.is_dir():
            shutil.copytree(srcdir, destdir)
            print('fin')
    else:
        if not srcdir.exists():
            print(f'{srcdir} does not exist')
        if destdir.exists():
            print(f'{destdir} exists')


# 讀取xml設定檔
def readxml(filepath):

    pass


# 取得最後一次的資料夾序號
def getlastno(keyword):
    pass


# 產生新的資料夾名稱
def gendirname(postfix):
    pass


rootDir = "c:\\Temp"
p = Path(rootDir)
pjkeyword = "SAB"
emptyDirName = pjkeyword + "-空白"
destDirName = "01.SAB-109-1"
srcDir = p / emptyDirName
destDir = p / destDirName

copydirs(srcDir, destDir)
