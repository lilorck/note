# Form & ModelForm

Form和ModelForm的区别在：

- Form：需要吧model.py中模型的字段重新定义一边，插件需要手动添加
- ModelForm：定义需要展示的字段，不要想一个一个的定义，能批量添加插件

## model.py的模型类

根据数据库的表设计模型类

```python
# -*- coding: utf8 -*-
# @author: Roc Sun
# @email: 599849606@qq.com

from django.db import models


class UserInfo(models.Model):
    """
    Attributes:
        phone: unique
    """

    your_name = models.CharField(max_length=4, null=True, blank=True, verbose_name='姓名')
    username = models.CharField(max_length=8, null=False, blank=False, verbose_name='用户名')
    password = models.CharField(max_length=16, null=False, blank=False, verbose_name='密码')
    email = models.EmailField(max_length=32, null=True, blank=True, verbose_name='邮箱')
    phone = models.CharField(max_length=4, null=True, blank=True, verbose_name='电话', unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


class Article(models.Model):
    """
    article
    Attributes:
    """

    title = models.CharField(max_length=32, null=False, blank=False, verbose_name='文章标题')
    describe = models.CharField(max_length=255, null=False, blank=False, verbose_name='描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    text = models.TextField()
    user = models.ForeignKey(to='UserInfo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Comment(models.Model):
    """
    comment
    """

    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article')
    content = models.CharField(max_length=255, null=False, blank=False, verbose_name='评论')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

```
