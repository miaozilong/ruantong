from flask import Flask

app = Flask(__name__)


# Flask类的route()函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。
@app.route(rule='/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    # app.run(host, port, debug, options)
    #
    # host
    # 要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
    #
    # port
    # 默认值为5000
    #
    # debug
    # 默认为false。 如果设置为true，则提供调试信息
    app.run(host='localhost', port=80, debug=True)
