import requests

if __name__ == '__main__':
    # 目标 url
    url = 'https://www.baidu.com'
    # 发送 get 请求，获取响应信息
    response = requests.get(url)
    response.encoding = "UTF-8"
    # 打印响应信息
    print('状态码：', response.status_code)
    print('响应头：', response.headers)
    print('cookie：', response.cookies)
    print('响应的 URL：', response.url)
    print('是否跳转：', response.is_redirect)
    print('响应的状态：', response.ok)
    print('响应内容（文本格式）：\n', response.text)
