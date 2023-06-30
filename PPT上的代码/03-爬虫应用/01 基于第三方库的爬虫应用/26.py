from bs4 import BeautifulSoup

if __name__ == '__main__':
    # with open('24.html', 'r', encoding='UTF-8') as f:
    #     print(f.read())
    f = open('24.html', encoding='UTF-8')
    text = f.read()
    # print(text)
    f.close()
    bs = BeautifulSoup(text, 'html.parser')
    # 获取第一个 div 标签中的所有内容
    # print(bs.div)
    print(bs.div.name)
    print(bs.div.attrs)
    # 获取到第一个p节点
    # print(bs.p.string)
    # 获取标签的内容，不包含注释符号
    print(bs.a.string)
    for i in bs.body.children:
        print(i)
        print()