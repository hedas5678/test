import shutil
from pathlib import Path
from xml.dom.minidom import parse
import xml.dom.minidom

# xml.etree.ElementTree 筆記
# https://hackmd.io/@top30339/rJYlKYpml?type=view
# 用 ElementTree 在 Python 中解析 XML
# https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/processing-xml-in-python-with-element-tree.html
# Python/XML工具
# https://zh.m.wikibooks.org/zh-tw/Python/XML%E5%B7%A5%E5%85%B7
# 深入解讀Python解析XML的幾種方式
# https://kknews.cc/zh-tw/news/nmb8j2.html
#
# https://jennaweng0621.pixnet.net/blog/post/403511006-%5Bpython%5D-%E8%AE%80%E5%8F%96xml%E6%AA%94
# XML parsing
# https://docs.python-guide.org/scenarios/xml/
# 20.5. xml.etree.ElementTree — The ElementTree XML API
# https://docs.python.org/3.4/library/xml.etree.elementtree.html
#



filepath = "C:\\Users\\cctsai\\PycharmProjects\\filesystem-demo\\copyTemplate\\Setting.xml"
# 使用minidom解析器打开 XML 文档
p = Path(filepath)
if not p.exists():
    print(p, " does not exist.")
if not p.is_file():
    print(p, " isn't a file.")
DOMTree = xml.dom.minidom.parse(filepath)
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    s = collection.getAttribute("shelf")
    print(f"Root element : {s}")
# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")
# 打印每部电影的详细信息
elements = {"type", "format", "year", "rating", "stars", "description"}

for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        title = movie.getAttribute("title")
        print(f"Title : {title}")
        # print(type(title))
        dict={"type":""}
    for element in elements:
        tag = movie.getElementsByTagName(element)[0]
        value = tag.childNodes[0].data
        dict[element] = value
        if element == "type":
            typee =dict.get("type")
            print(f"type : {typee}")
