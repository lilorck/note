# split方法

`split()`方法是用于切割字符串，切割后生成列表。传入切割符默认切所有的。

语法：

> str.split(str='', num=string.count(str))

参数：

- str：切割符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
- num：切割次数

返回值：

- 返回值是一个列表

实列：

```python
s = 'ssss.md.txt'


def split_many(filename):
    return '.' in filename and \
           filename.split('.')[1]


def split_one(filename):
    return '.' in filename and \
           filename.split('.', 1)[1]


print(split_many(s))
print(split_one(s))
```

打印结果：

```dos
md
md.txt
```
