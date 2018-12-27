# 定制404响应页面

通过调用装饰器`errorhandler()`函数绑定需要返回的自制404页面即可，如果路由匹配为匹配到，直接返回绑定的404页面。

application.py:

```python
from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def root():
    return 'root page'


@app.errorhandler(404)
def login(error):
    return render_template('404page.html'), 404


if __name__ == '__main__':
    app.run()
```

templates中的`404page.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404</title>
</head>
<body>
    <h1>This is 404 page</h1>
</body>
</html>
```

**注：**
使用errorhandler