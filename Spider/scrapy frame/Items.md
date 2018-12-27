# Scrapy----Items

爬取的主要目标就是从非结构性的数据源提取结构性数据，例如网页。 Scrapy spider可以以python的dict来返回提取的数据.虽然dict很方便，并且用起来也熟悉，但是其缺少结构性，容易打错字段的名字或者返回不一致的数据，尤其在具有多个spider的大项目中。。

为了定义常用的输出数据，Scrapy提供了 Item 类。 Item 对象是种简单的容器，保存了爬取到得数据。 其提供了 类似于词典(dictionary-like) 的API以及用于声明可用字段的简单语法。

许多Scrapy组件使用了Item提供的额外信息: exporter根据Item声明的字段来导出数据、 序列化可以通过Item字段的元数据(metadata)来定义、 trackref 追踪Item实例来帮助寻找内存泄露 (see 使用 trackref 调试内存泄露) 等等。</br>
类似在ORM中做的一样，您可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field 的类属性来定义一个Item。 (如果不了解ORM, 不用担心，您会发现这个步骤非常简单)

## 声明Item

在items.py中使用`class`定义类以及`Field`对象来声明。

```python
import scrapy


class Model_(scrapy.Item):
    variable = scrapy.Field()
```

**注：</br>**
Scrapy Item定义方式与 Django Models 很类似, 不过没有那么多不同的字段类型(Field type)，更为简单
