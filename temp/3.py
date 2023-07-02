import numpy as np
from bs4 import BeautifulSoup

import requests

if __name__ == '__main__':
    cookies = {
        'f': 'n',
        'commontopbar_new_city_info': '984%7C%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90%7Cxj',
        'commontopbar_ipcity': 'xj%7C%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90%7C0',
        'userid360_xml': '627EA9618BED6F2254F4192988C12129',
        'time_create': '1690886375269',
        'id58': 'CroOkmShU+UrDxkXFLDTAg==',
        'f': 'n',
        'wmda_uuid': '6c43f4d3b49738cc53052df13353d143',
        'wmda_new_uuid': '1',
        'wmda_session_id_11187958619315': '1688294376641-39b94e19-bd99-5555',
        'wmda_visited_projects': '%3B11187958619315',
        'crmvip': '',
        'dk_cookie': '',
        'PPU': 'UID=49872881527061&UN=0b2d1kwcb&TT=915cdd79cd5671a77c6c1d07a0b584f6&PBODY=LoMbhDGJDgxN5rOUeKS6NiOzsfv-1yYUQpQQVEHf6ydzlpz6keP4ERmd93wT7rln0uRy2FUOsC-qgf_NZE7JXiqJpF0fduFKB93hCbT2AiHlkYfLPhed2QW5MoXuTCCLciafyQjRrq5RfW-f61HFHxX2GjLKMjVZiNL4GlLDY2k&VER=1&CUID=4RkKmHkOSMHlrtF7YEgYSA',
        'www58com': 'UserID=49872881527061&UserName=0b2d1kwcb',
        '58cooper': 'userid=49872881527061&username=0b2d1kwcb',
        '58uname': '0b2d1kwcb',
        'passportAccount': 'atype=0&bstate=0',
        'xxzl_cid': '2ca16902173d43c7a76f676fe28c10fc',
        'xxzl_deviceid': '1RrpjvZjKldzFgWfmZmE84MkoAlkCyiJduT9VperS9T7UWpe0j9V0uZo0SyCQZhE',
    }

    headers = {
        'authority': 'xj.58.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'f=n; commontopbar_new_city_info=984%7C%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90%7Cxj; commontopbar_ipcity=xj%7C%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90%7C0; userid360_xml=627EA9618BED6F2254F4192988C12129; time_create=1690886375269; id58=CroOkmShU+UrDxkXFLDTAg==; f=n; wmda_uuid=6c43f4d3b49738cc53052df13353d143; wmda_new_uuid=1; wmda_session_id_11187958619315=1688294376641-39b94e19-bd99-5555; wmda_visited_projects=%3B11187958619315; crmvip=; dk_cookie=; PPU=UID=49872881527061&UN=0b2d1kwcb&TT=915cdd79cd5671a77c6c1d07a0b584f6&PBODY=LoMbhDGJDgxN5rOUeKS6NiOzsfv-1yYUQpQQVEHf6ydzlpz6keP4ERmd93wT7rln0uRy2FUOsC-qgf_NZE7JXiqJpF0fduFKB93hCbT2AiHlkYfLPhed2QW5MoXuTCCLciafyQjRrq5RfW-f61HFHxX2GjLKMjVZiNL4GlLDY2k&VER=1&CUID=4RkKmHkOSMHlrtF7YEgYSA; www58com=UserID=49872881527061&UserName=0b2d1kwcb; 58cooper=userid=49872881527061&username=0b2d1kwcb; 58uname=0b2d1kwcb; passportAccount=atype=0&bstate=0; xxzl_cid=2ca16902173d43c7a76f676fe28c10fc; xxzl_deviceid=1RrpjvZjKldzFgWfmZmE84MkoAlkCyiJduT9VperS9T7UWpe0j9V0uZo0SyCQZhE',
        'pragma': 'no-cache',
        'referer': 'https://callback.58.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get('https://xj.58.com/chuzu/pn0/', cookies=cookies, headers=headers)

    response.encoding = 'utf-8'
    html = response.text
    print(html)
    f = open('a.html', 'w')
    f.write(html)
    f.close()
    bs = BeautifulSoup(html, 'html.parser')
