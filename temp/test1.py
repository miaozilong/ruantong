import requests
from bs4 import BeautifulSoup

def main():
    url ="https://www.dongchedi.com/auto/library/x-x-x-x-x-x-4-x-x-x-x"
    headsers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headsers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find('ul', class_='car-list_root__3bcdu')
    # print(a)
    b1 = a.find_all('li') # <class 'bs4.element.ResultSet'>
    b2 = a.contents # 效果相同 list
    b3 = a.children  # <class 'list_iterator'>

    # 方式1
    for item in b1:
        # print(type(item)) # <class 'bs4.element.Tag'>, Tag类型就可以使用select/find/find_all
        # a = item.select('span')
        a = item.find_all('span')
        # print(a[0].string)
    # 方式2
    for item in b2:
        # print(type(item)) # <class 'bs4.element.Tag'>
        a = item.select('span')
        # print(a[0].text)
        # print(a[0].string)
    # 方式3
    for item in b3:
        # print(item)
        # print(type(item)) # <class 'bs4.element.Tag'>
        a = item.find('span')
        # print(a.text)
    # 方式4
    for item in b2:
        # item = str(item)
        # print(type(item))
        bs = BeautifulSoup(str(item), 'html.parser')

        a = bs.find_all('span')
        print(a[0].text)


main()