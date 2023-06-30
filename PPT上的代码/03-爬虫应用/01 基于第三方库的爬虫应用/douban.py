import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    cookies = {
        'bid': 'oM2a6OtrYpU',
        '_pk_id.100001.4cf6': '4667473fb5d00bc6.1688008968.',
        '_pk_ses.100001.4cf6': '1',
        'ap_v': '0,6.0',
        '__utma': '30149280.1244496996.1688008968.1688008968.1688008968.1',
        '__utmb': '30149280.0.10.1688008968',
        '__utmc': '30149280',
        '__utmz': '30149280.1688008968.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utma': '223695111.404157462.1688008968.1688008968.1688008968.1',
        '__utmb': '223695111.0.10.1688008968',
        '__utmc': '223695111',
        '__utmz': '223695111.1688008968.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'bid=oM2a6OtrYpU; _pk_id.100001.4cf6=4667473fb5d00bc6.1688008968.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1244496996.1688008968.1688008968.1688008968.1; __utmb=30149280.0.10.1688008968; __utmc=30149280; __utmz=30149280.1688008968.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.404157462.1688008968.1688008968.1688008968.1; __utmb=223695111.0.10.1688008968; __utmc=223695111; __utmz=223695111.1688008968.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'start': '0',
    }
    # response = requests.get('https://movie.douban.com/top250', params=params, cookies=cookies, headers=headers)
    # response.encoding = 'UTF-8'
    # print(response.text)
    # f = open('douban0.html', 'w', encoding='UTF-8')
    # f.write(response.text)
    # f.close()
    text = ''
    with open('douban0.html', encoding='UTF-8') as f:
        text = f.read()
    bs = BeautifulSoup(text, 'html.parser')
    movie_data = bs.find(name='ol', attrs={'class': 'grid_view'}).find_all('div', class_='info')
    datalist = []
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
        print()
