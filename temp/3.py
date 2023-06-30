from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("3.html", encoding='UTF-8') as fp:
        html = fp.read()
    # print(html)
    # 使用BeautifulSoup来解析html
    # 参数1：需要被解析的内容 参数2：解析方式
    bs = BeautifulSoup(html, "html.parser")
    print(bs.title)
    print(bs.tilte.string)
    # 根据tagname查找第一个元素 标签：写在< >中的就是标签
    print(bs.div)
    # 输出标签里的属性 字典类型
