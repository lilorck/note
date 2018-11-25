# URL路由注册

Flask中的URL路由是通过个一个装饰器函数`route()`，将相关的函数和URL关联起来。

## 路由的注册

在路由系统中定义规则可以的方法可以概括为三种:

1. 使用 flask.Flask.route() 装饰器
2. 使用 flask.Flask.add_url_rule() 函数
3. 直接访问暴露为 flask.Flask.url_map 的底层的Werkzeug路由系统

### flask.Flask.route()装饰器

`route()`装饰器中调用的是`add_url_rule()`函数，实现路由的绑定。

`route()`官方文档API：

> route(rule, **options)
> A decorator that is used to register a view function for a given URL rule. This does the same thing as add_url_rule() but is intended for decorator usage:

```
@app.route('/')
def index():
    return 'This is test page!'
```

> 参数:	
- rule – the URL rule as string
- endpoint – the endpoint for the registered URL rule. Flask itself assumes the name of the view function as endpoint
- options – the options to be forwarded to the underlying Rule object. A change to Werkzeug is handling of method options. methods is a list of methods this rule should be limited to (GET, POST etc.). By default a rule just listens for GET (and implicitly HEAD). Starting with Flask 0.6, OPTIONS is implicitly added and handled by the standard request handling.

### flask.Flask.add_url_rule()函数

在装饰器`route()`的内部调用执行，直接调用需要传入:

1. url:string格式
2. endpoint:函数别名
3. view_func:视图函数，即与URL绑定的函数

上边的代码相当于下边的这段代码

```python
from flask import Flask

app = Flask(__name__)


def define_view_func(*args, **kwargs):
    """
    define a function that is used to view function
    :param args: none
    :param kwargs: none
    :return: string
    """
    print(args)
    print(kwargs)
    return 'This is test page!'


app.add_url_rule('/', 'define_view_func', define_view_func)

if __name__ == '__main__':
    app.run(debug=True)

```

**如果提供了view_func参数，则会使用endpoint别名进行过注册，如果没有提供view_func，则需使用`flask.Flask.view_functions()`创建一个函数别名。**

```python
app.view_functions['define_view_func'] = define_view_func
app.add_url_rule('/', 'define_view_func', define_view_func)
```

### flask.Flask.url_map 的底层的Werkzeug路由系统

该方法是根据需求自定义规则，生成目标的数据类型。使用该方法是需要自定义一个类。

```python
from flask import Flask
from werkzeug.routing import BaseConverter


class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value)
                        for value in values)


app = Flask(__name__)
app.url_map.converters['list'] = ListConverter

```
