# Flask的安装及快速使用

## 创建flask的虚拟环境

```dos
F:\venv>virtualenv --no-site-packages -p C:\Python36\python.exe flask-env
Running virtualenv with interpreter C:\Python36\python.exe
Using base prefix 'C:\\Python36'
New python executable in F:\venv\flask-env\Scripts\python.exe
Installing setuptools, pip, wheel...
done.
```

## 安装flask

通过pip安装

```dos
F:\venv>flask-env\Scripts\activate

(flask-env) F:\venv>pip install flask
Collecting flask
  Using cached https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl
Collecting click>=5.1 (from flask)
  Using cached https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.14 (from flask)
  Using cached https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl
Collecting Jinja2>=2.10 (from flask)
  Using cached https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl
Collecting itsdangerous>=0.24 (from flask)
  Using cached https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10->flask)
  Using cached https://files.pythonhosted.org/packages/9d/80/9a5daf3ed7b8482e72ee138cef602b538cfba5c507e24e39fb95c189b16b/MarkupSafe-1.1.0-cp36-cp36m-win_amd64.whl
Installing collected packages: click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, flask
Successfully installed Jinja2-2.10 MarkupSafe-1.1.0 Werkzeug-0.14.1 click-7.0 flask-1.0.2 itsdangerous-1.1.0

```

## 快速启动一个flask项目

新建一个py文件，导入flask，只需要三行代码就能启动一个项目

```python
from flask import Flask


app = Flask(__name__)

app.run()
```

正常的flask项目包含路由:

```python
from flask import Flask


obj = Flask(__name__)


@obj.route('/')
def roots():
    return 'Root page'


if __name__ == '__main__':
    obj.run()

```