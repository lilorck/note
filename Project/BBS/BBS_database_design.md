# BBS数据库设计

设计一个简单的BBS论坛的数据库，表与表之间的关系

## BBS实现的功能

设计的BBS要求实现以下的功能需求：

1. 账户
2. 好友模块
3. 评论
4. 文章

## 账户

账户模块包含用户信息，找回密码，头像。设计为UserInfo表，见下设计：</br>

1. 用户名
    - usernme `archar null=Fasle unique=Ture`
2. 密码
    - password `varchar 8~16 null=False`
3. 性别
    - gender `bool default=Ture`
4. 邮箱
    - email `email null=False`
5. 电话
    - phone `varchar2`
6. 地址
    - adress `varchar 128`
