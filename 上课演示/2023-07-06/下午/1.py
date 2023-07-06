from flask import Flask

# 创建web应用
# __name__ 当前文件
app = Flask(__name__)


# 指定url匹配地址
# 使用app.router注解中的rule指定地址
@app.route(rule='/')
def hello_world():
    return 'hello world! <br /> 你好世界'


# 再次启动时,如果启动报错,需要结束所有的python.exe文件
if __name__ == '__main__':
    # 默认flask是关闭调试模式的,需要指定为打开
    # flask的调试模式打开后,会打印相关的web应用信息
    # host 表示Web应用的主机名,默认是127.0.0.1或者localhost 可以指定网卡的IP,也可以使用0.0.0.0表示所有的ip
    # port 表示web应用的端口,默认为5000   如果端口冲突会报错  端口的范围是1到65535  尽量使用1024之后的端口
    app.run(host='0.0.0.0', port=50090, debug=True)
