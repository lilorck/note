# URL路由注册

在路由系统中定义规则可以的方法可以概括为三种:

1. 使用 flask.Flask.route() 装饰器
2. 使用 flask.Flask.add_url_rule() 函数
3. 直接访问暴露为 flask.Flask.url_map 的底层的 Werkzeug 路由系统

