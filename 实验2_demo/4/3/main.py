import requests
from bs4 import BeautifulSoup
import re
import xlwt

# 1-下载网页
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    # 携带头部信息发送get请求
    response = requests.get(url, headers=headers)
    return response.text

# 2-解析数据
def get_data(baseurl):
    datalist = []
    # 循环获取，1页25部，共10页
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = get_html(url)

        # 解析数据
        bs = BeautifulSoup(html, "html.parser")
        movie_data = bs.find('ol', class_='grid_view').find_all('div', class_='info')
        for item in movie_data:
            data = []
            # 使用bs获取影片名字
            title = item.find('span', class_='title').string
            data.append(title)
            # 使用bs获取影片评分
            score = item.find('span', class_='rating_num').string
            data.append(score)
            # 影片评价人数正则
            people_pattern = re.compile(r'<span>(\d*)人评价</span>')
            # 使用正则获取影片评分人数
            people = re.findall(people_pattern, str(item))[0]
            data.append(people)
            # 影片相关信息正则
            context_pattern = re.compile(r'<p class="">(.*?)</p>', re.S)
            # 使用正则获取影片相关信息
            content = re.findall(context_pattern, str(item))[0]
            # 去掉</br>和/
            content = re.sub("<br(\s+)?/>(\s+)?", " ", content)
            content = re.sub("/", " ", content)
            data.append(content.strip())
            datalist.append(data)
    return datalist

# 3-保存数据，相关内容将在第7章详细介绍
def saveData(datalist, savepath):
    # 创建workbook对象
    book = xlwt.Workbook(encoding="utf-8")
    # 创建工作表
    sheet = book.add_sheet("豆瓣电影top250", cell_overwrite_ok=True)
    col = ('电影名称', '评分', '评价人数', '相关信息')
    # 列名
    for i in range(0, 4):
        sheet.write(0, i, col[i])
    # 保存电影数据
    for i in range(1, 251):
        for j in range(0, 4):
            sheet.write(i, j, datalist[i - 1][j])
    book.save(savepath)

# 程序入口
def start():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = get_data(baseurl)
    saveData(datalist, 'D:\doubai.xls')

if __name__ == '__main__':
    # 调用入口程序
    start()
