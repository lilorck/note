# URL路由系统

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

**如果提供了view_func参数，则会注册为别名endpoint，如果没有提供view_func，则需使用`flask.Flask.view_functions()`创建一个函数别名。**

```python
app.view_functions['define_view_func'] = define_view_func
app.add_url_rule('/', define_view_func)
```

### flask.Flask.url_map 的底层的Werkzeug路由系统

该方法是根据需求自定义规则，生成目标的数据类型。使用该方法是需要自定义一个类，继承BaseConverter。然后注册为默认转换器。

```python
from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)
app.debug = True


# 自定义一个函数转换器
class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value)
                        for value in values)


# 将写好的类注册到DEFAULT_CONVERTERS
app.url_map.converters['list'] = ListConverter


@app.route("/<list:params>")
def demo(params):
    return 'Demo page,params is %s' % params


if __name__ == '__main__':
    app.run()

```

## 变量规则

要给URL添加变量部分，你可以把这些特殊的字段标记为`<variable_name>`。默认情况下，URL 中的变量部分接受任何不带斜线的字符串，而`<converter:variable_name>`也可以指定不同的转换器。变量部分以关键字参数传递给视图函数。

| URL参数 | |
| ------ | ------ |
|string	|接受任何不带斜线的字符串（默认的转换器）
|int	|接受整数
|float	|同 int ，但是接受浮点数
|path	|和默认的相似，但也接受斜线
| |

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

需要注意的一个重要细节是 Flask 处理结尾斜线的方式。你可以应用下面两个规则来保证 URL 的唯一:

1. 如果规则以斜线结尾，当用户以不带斜线的形式请求，用户被自动重定向到带有结尾斜线的相同页面。
2. 如果规则结尾没有斜线，当用户以带斜线的形式请求，会抛出一个 404 not found 。

这与 web 服务器处理静态文件的方式一致。这使得安全地使用相对链接地址成为可能。

***你可以为同一个函数定义多个规则。无论如何，他们也要唯一。也可以给定默认值。 这里给出一个接受可选页面的 URL 定义:***
```python
@app.route('/users/', defaults={'page': 1})
@app.route('/users/page/<int:page>')
def show_users(page):
    pass
```

以下是 route() 和 add_url_rule() 接受的参数。两者唯一的区别是，带有路由参数的视图函数用装饰器定义，而不是 view_func 参数。

|rule | URL规则的字符串 |
| ------ | ------ |
| endpoint	| 注册的 URL 规则的末端。如果没有显式地规定，Flask 本身假设末端的名称是视图函数的名称，。
| view_func	| 当请求呈递到给定的末端时调用的函数。如果没有提供，可以在用在 view_functions 字典中以末端作为键名存储，来在之后设定函数。
| defaults	| 规则默认值的字典。上面的示例介绍了默认值如何工作。
| subdomain	| 当使用子域名匹配的时候，为子域名设定规则。如果没有给定，假定为默认的子域名。
| **options	| 这些选项会被推送给底层的 Rule 对象。一个 Werkzeug 的变化是 method 选项的处理。methods是这个规则被限定的方法列表（ GET ， POST 等等）。默认情况下，规则只监听 GET （也隐式地监听 HEAD ）。从 Flask 0.6 开始，OPTIONS 也被隐式地加入，并且做标准的请求处理。 它们需要作为关键字参数来给定。

## 唯一 URL / 重定向行为

即如果访问的路由的结尾没有带“/”，服务器会返回一个重定向路由，在该路由的末尾加上“/”，让浏览器重新访问。

**如果配置的是严格URL，会返回404页面**

```python
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/user/', defaults={'page': 1})
@app.route('/user/<int:page>')
def user_page(page):
    return f"user page {page}"


if __name__ == '__main__':
    app.run()

```

访问`127.0.0.1:5000/user`,服务器后台的打印结果：

```shell
127.0.0.1 - - [26/Nov/2018 17:23:31] "GET /user HTTP/1.1" 301 -
127.0.0.1 - - [26/Nov/2018 17:23:31] "GET /user/ HTTP/1.1" 200 -
```

返回301状态码，让浏览器重新访问。在Response头中会多出一个`Location: http://127.0.0.1:5000/user/`。

**注：**
> 301:永久重定向 </br>
> 302:临时重定向

## 构造URL

所谓的构造URL就是根据函数名去找路由地址。

构造URL的优势：

```python
from flask import Flask, url_for, redirect

app = Flask(__name__)
app.debug = True


@app.route('/')
def root():
    return 'Root page'


@app.route('/login')
def login():
    url = url_for('root')
    print('in login function')
    return redirect(url)


@app.route('/last')
def last():
    url = url_for('login')
    print('in last function')
    return redirect(url)


if __name__ == '__main__':
    app.run()

```

1. 反向构建通常比硬编码的描述性更好。更重要的是，它允许你一次性修改 URL， 而不是到处边找边改。
2. URL 构建会转义特殊字符和 Unicode 数据，免去你很多麻烦。
3. 如果你的应用不位于 URL 的根路径（比如，在 /myapplication 下，而不是 / ）， url_for() 会妥善处理这个问题。

## 定义route()中的HTTP请求方式

HTTP有许多不同的访问URL方法。默认情况下，路由只回应`GET`请求，但是通过`route()`装饰器传递methods参数可以改变这个行为。

- method是一个list

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```