# Django总结

## 什么是WSGI

&nbsp;&nbsp;&nbsp;&nbsp; `WSGI:`全称是`Web Server Gateway Interface`,是一种规范，描述web server如何与web application通信的规范,Django，Flask是实现了WSGI application协议的web框架.

## 什么是http协议

HTTP:Hyper Text Transfer Protocol，超文本传输协议，是一种建立在TCP上的无状态连接，包含有请求头和请求体

## Django路由系统中都涉及哪些知识点

Django路由系统中都涉及哪些知识点以下知识点：

1. 请求的流程
2. url的解析和匹配
3. 路由分发
4. URL的命名和逆向解析
5. 请求的响应

## FBV CBV本质区别和联系

### FBV

FBV：function based view，基于函数的视图

### CBV

CBV：class based view，基于类的视图

### 区别和联系

本质上都是函数，非要说有区别的话：

1. cvb比较简洁，GET/POST 等业务功能分别放在不同的get/post函数中，
2. fbv需要自己做判断进行区分。

## 列举Django 20个ORM操作

filter(),get(),all(),exclude(),order_by(),reverse(),distinct(),first(),last(),delete(),exists(),count()

## Django是否能执行原生sql?如果能，请列举出所有的

django可以执行原生sql
django orm 中三种能写sql语句的方法
原生sql --> connection

```python
from django.db import connection, connections
cursor = connection.cursor() #cursor = connection['default'].cursor()
cursor.execute("""SELECT * from auth_user where id = %s""", [1])
row = cursor.fetchone()  #fetchall()/fetchmany(...)
```

## 简述Django中间件以及中间件的方法及应用场景

中间件对所有的请求进行批量处理，在视图函数执行前后进行自定义操作。方法：</br>
process_request</br>
process_response</br>
process_view,</br>
process_template_response,</br>
process_exception </br>
场景：登录注册，权限设置，cors跨域，缓存问题

## 比较Django中Form和Modelform的区别

form对于字段的设计只能手动进行，modelform可以对多个字段批量进行设置,也可以根据models.py中的类来设置

## 简述session的实现原理

session依赖于cookie来实现的，cookie是保存在浏览器端的键值对，而session是保存服务器端的键值对，但依赖于cookie,（也可以不依赖于cookie，可以放在url,或请求头，但是没有cookie方便。</br>
实现过程：session认证成功后，产生一堆随机字符串，传给客户端cookie进行保存，再次访问时，根据请求携带的cookie保存的键值对进行认证。

## 简述权限组件的实现流程

1. 在web应用中，一个url代表一个权限，可访问某一url则说明有该权限，该权限系统中，url被分为两种，一种是可以做菜单的的父级权限，一种是不能做菜单的子权限，Menu表中的数据被称为一级菜单，二级菜单被分配给一级菜单。子权限分配给父权限。
2. 当用户登陆成功时，根据用户所有的角色，查询出所具有的权限，将权限信息和菜单信息放入到session中，登录成功后，跳转至其他URL时，请求经过中间件进行权限的检验，根据当前访问的url和session中存放的权限信息进行正则匹配，都匹配不成，则拒绝访问。匹配成功，则继续走正常的流程，得到相应的响应。
3. 页面中可点击的按钮也是权限，在模板渲染时使用自定义filter判断该按钮所代表的权限是否在该用户所在的权限中，如果是，则显示按钮，否则不显示。

## 默写权限所涉及的所有表以及所有的表关系

三个类五张表：用户表，权限表，角色表，用户角色表，角色权限表 </br>
用户表与角色表：多对多
角色表与权限表：多对多

## Django中 filter  simple_tag inclution的区别

filter：</br>
根据条件展示相对用的HTML内容
simple_tag: </br>
和自定义filter类似，只不过接收更灵活的参数
inclution
多用于返回THML代码段

## 列出CRM你了解的所有的业务流程（文字描述）

用户登录，根据角色获得对应的权限，业务权限有对客户的化为公户，公户申请变成私户</br>
对私户的顾客进行资料进行增，改，查，对于客户添加跟踪信息，更新客户更新状态</br>
批量处理，批量更新，上传文件