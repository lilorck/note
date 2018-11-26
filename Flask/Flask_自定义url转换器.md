# 自定义URL转换器

实现自定义URL转换器，转换成目标数据类型，比如list，dict等

## BaseConverter类

flask中的所有的URL的参数的类型都是基于`BaseConverter`类实现的，自定义的转换器需要重构该类的`to_python()`和`to_url()`两个方法即可。源码：

```python
class BaseConverter(object):

    """Base class for all converters."""
    regex = '[^/]+'
    weight = 100

    def __init__(self, map):
        self.map = map

    def to_python(self, value):
        return value

    def to_url(self, value):
        return url_quote(value, charset=self.map.charset)

```

其中to_python方法的作用就是将你传过去的参数转换成对应类型的数据，比如你设置传参是uuid类型数据，那么当你传参以后，就会调用to_python方法，将参数转换为对应的uuid类型。
而to_url方法就是将从to_python方法中获得的转换成目标url地址

## 注册到DEFAULT_CONVERTERS

通过`app.url_map.converters['list'] = ListConverter`将自定义的转换器注册到DEFAULT_CONVERTERS中

```python
from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)
app.debug = True


class ListConverter(BaseConverter):

    # 自定义生成目标数据类型
    def to_python(self, value):
        return value.split(',')

    # 自定义生成目标url
    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value)
                        for value in values)


# 注册到DEFAULT_CONVERTERS
app.url_map.converters['list'] = ListConverter


print(app.url_map.converters)


@app.route("/<list:params>")
def demo(params):
    return 'Demo page,to_url is %s' % params


if __name__ == '__main__':
    app.run()
```

控制台中：

```dos
FLASK_APP = WerkzeugUrlMap.py
FLASK_ENV = development
FLASK_DEBUG = 0
In folder F:/FlaskProject/MyTestFlask
F:\venv\flask-venv\Scripts\python.exe -m flask run
 * Serving Flask app "WerkzeugUrlMap.py"
 * Environment: development
 * Debug mode: off
{'default': <class 'werkzeug.routing.UnicodeConverter'>, 'string': <class 'werkzeug.routing.UnicodeConverter'>, 'any': <class 'werkzeug.routing.AnyConverter'>, 'path': <class 'werkzeug.routing.PathConverter'>, 'int': <class 'werkzeug.routing.IntegerConverter'>, 'float': <class 'werkzeug.routing.FloatConverter'>, 'uuid': <class 'werkzeug.routing.UUIDConverter'>, 'list': <class 'WerkzeugUrlMap.ListConverter'>}
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [26/Nov/2018 21:12:36] "GET /1,2,4 HTTP/1.1" 200 -
···
