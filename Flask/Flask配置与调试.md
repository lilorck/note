# Flask的配置与调试

总结Flask中的配置与调试：

- 配置管理
- 调试模式

## 配置管理

复杂的项目需要配置各种环境。如果设置项很少，可以直接硬编码进来，比如下面的方式:

```python
app = Flask(__name__)
app.config['DEBUG'] = True
```

`app.config`是`flask.config.Config`类的实例，继承自Python内置数据结构dict,所以可以使用update方法：

```python
app.config.update(
    DEBUG = True,
    ...
)
```

`app.config`内置的全部配置变量可以参看`Builtin Configuration Values`。如果设置选项很多，想要集中管理设置项，应该将他们存放到一个文件里面。`app.config`支持多种更新配置的方式。假设现在有个叫做`settings.py`的配置文件，其中的内容如下：

```python
A = 1
```

可以选择如下三种方式加载:

- 通过配置文件加载

```python
# 通过模块名的字符串
app.config.from_object('settings')  

# 或者:
import settings
app.config.from_object(settings)
```

- 通过文件名字加载。但是不限于只使用.py后缀的文件名

```python
# slient=True该文件不存在时不抛异常，返回False,默认是会抛出异常
app.config.from_pyfile('settings.py',slient=True)
```

总结如下：

```python
# ==========方式一：============
 app.config['SESSION_COOKIE_NAME'] = 'session_lvning'  #这种方式要把所有的配置都放在一个文件夹里面，看起来会比较乱，所以选择下面的方式
# ==========方式二：==============
app.config.from_pyfile('settings.py')  #找到配置文件路径，创建一个模块，打开文件，并获取所有的内容，再将配置文件中的所有值，都封装到上一步创建的配置文件模板中

print(app.config.get("CCC"))
# =========方式三：对象的方式============
 import os 
 os.environ['FLAKS-SETTINGS'] = 'settings.py'
 app.config.from_envvar('FLAKS-SETTINGS') 

# ===============方式四（推荐）：字符串的方式，方便操作，不用去改配置，直接改变字符串就行了 ==============
app.config.from_object('settings.DevConfig')

# ----------settings.DevConfig----------
from app import app
class BaseConfig(object):
    NNN = 123  #注意是大写
    SESSION_COOKIE_NAME = "session_sss"

class TestConfig(BaseConfig):
    DB = "127.0.0.1"

class DevConfig(BaseConfig):
    DB = "52.5.7.5"

class ProConfig(BaseConfig):
    DB = "55.4.22.4"
```
 
要想在视图函数中获取配置文件的值，都是通过`app.config`来拿。但是如果视图函数和Flask创建的对象app不在一个模块。就得通过导入来拿。可以不用导入。直接导入一个`current_app`，这个就是当前的app对象，用`current_app.config`就能查看到了当前app的所有的配置文件

```python
from flask import Flask,current_app

@app.route('/index',methods=["GET","POST"])
def index():
    print(current_app.config)   #当前的app的所有配置
    session["xx"] = "fdvbn"
    return "index"
```

## 调试模式

虽然`app.run()`这样的方式适用于启动本地的开发服务器，但是每次修改代码后都要手动重启的话，既不方便也不够优雅。如果启用了调试模式，服务器会在代码修改后自动重新载入，并在发生错误时提供一个能获得错误上下文及可执行代码的调试页面。 
有两种途径来启动调试模式:

直接在应用对象上设置:

```python
app.debug = True
app.run()
```

作为run的参数传入:

```python
app.run(debug=True)
``` 

需要注意，开启调试模式会成为一个巨大的安全隐患，因此他绝对不能用于生产环境中