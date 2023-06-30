import json
import requests
from urllib import request
if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    x = requests.get(url)
    text = x.text
    print(text)
    print(type(text))
    # 使用json.loads强转  结果可能是列表或者字典类型
    json_load = json.loads(text)
    print(json_load)
    print(type(json_load))
    # 反过来转换使用json.dumps
    dumps = json.dumps(json_load)
    f = open("a.json", "w")
    f.write(dumps)
    f.close()
    print()
