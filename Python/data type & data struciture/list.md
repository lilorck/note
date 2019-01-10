# 列表

列表是有序的可变的元素集合。列表中的每个元素可以使任何数据类型，包括列表本身。

## 列表生成

Python3中的列表通过以下几种方式生成

### 定义

直接通过中括号`[]`定义一个列表

```python
lis = [1, 2, 'a', [1, 2], (2,), {'key': 222}]
```

### for循环

```py
lis = []
for i in range(10):
    lis.append(i)
```

### 列表推导式

通过列表生成式`[表达式 for 变量 in 列表 [if 条件]]`来实现,其中if条件是可选条件。

```py
>>> lis = [i ** 3 for i in range(10) if i % 2 == 0]
>>> print(lis)
[0, 8, 64, 216, 512]
>>>
```

## 列表的切片，索引

列表通过索引的操作和字符串的操作一直，都能进行查询，切片，替换，逆向切片等操作，但是：字符串不能通过索引重新赋值，而list可以。可以通过切片进行重新赋值。

```py
>>> li = ['马拉多纳','外星人','小罗','内马尔']
>>> li[2:3] = ['卡卡','C罗','齐达内','兰帕德']
>>> li
['马拉多纳', '外星人', '卡卡', 'C罗', '齐达内', '兰帕德', '内马尔']
>>> li[2:5:2] = ['皮埃尔','佩佩']
>>> li
['马拉多纳', '外星人', '皮埃尔', 'C罗', '佩佩', '兰帕德', '内马尔']
>>>
```

## 列表内置方法

list的内置方法有以下11种，主要是增加，删除，查找，排序，复制，反转的功能：

- [append](#append)
- [insert](#insert)
- [extend](#extend)
- [copy](#copy)
- [count](#count)
- [remove](#remove)
- [pop](#pop)
- [clear](#clear)
- [sort](#sort)
- [reverse](#reverse)

### append

该方法是将某个元素添加到`list`中末尾。

```sh
>>> lis = []
>>> lis.append(1)
>>> lis.append(2)
>>> print(lis)
[1, 2]
>>>
```

### insert

该方法是将某个元素添加到`list`中指定的索引。

```sh
>>> lis.insert(2, 3)
>>> print(lis)
[1, 2, 3]
>>>
```

### extend

该方法是传入一个可迭代对象，然后把每个元素添加到调用该方法的列表中，字符串会拆成一个一个的字符，然后从最后添加进去，只是把第一层添加进去，不会把嵌套的拆开。源码：

```py
def extend(self, iterable): # real signature unknown; restored from __doc__
    """ L.extend(iterable) -> None -- extend list by appending elements from the iterable """
    pass
```

实例：

```sh
>>> lis = [1, 2, 3]
>>> li = [4, 5, 6]
>>> lis.extend(li)
>>> print(lis)
[1, 2, 3, 4, 5, 6]
>>> lis.extend('789')
>>> print(lis)
[1, 2, 3, 4, 5, 6, '7', '8', '9']
>>> print(lis)
[1, 2, 3, 4, 5, 6, '7', '8', '9']
>>> li = [10, [11, 12], 13]
>>> lis.extend(li)
>>> print(lis)
[1, 2, 3, 4, 5, 6, '7', '8', '9', 10, [11, 12], 13]
>>>
```

### copy

对list进行浅拷贝。返回一个拷贝的列表。

```sh
>>> print(lis)
[3, 5, 6, '7', [11, 12], 10, 4, '9', 13, '8']
>>> lis2 = lis.copy()
>>> print(lis, lis2)
['8', 13, '9', 4, 10, [11, 12], '7', 6, 5, 3]
['8', 13, '9', 4, 10, [11, 12], '7', 6, 5, 3]
>>> lis is lis2
False
>>>
```

### index

该方法是查找`list`中指定区间内的元素的索引，默认区间是全部列表。如果有，返回第一个找到的索引，反之，抛出ValueError异常。源码：

```py
def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
    """
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
    """
    return 0
```

实例：

```sh
>>> lis
[1, 2, 3, 3]
>>> lis.index(3)
2
>>> lis[3] = 4
[1, 2, 3, 4]
```

### count

计算某个元素在list中出现的次数。如果不存在返回0。实例：

```sh
>>> print(lis)
[1, 2, 3, 4, 5, 6, '7', '8', '9', 10, [11, 12], 13] 
>>> lis.count('1')
0
>>> lis.count(6)
1
>>>
```

### remove

该方法是删除第一个匹配到的指定的元素，如果不存在，抛出`ValueError`异常。该方法没有返回值。

```sh
>>> print(lis)
[2, 3, 5, 6, '7', [11, 12], 10, 4, '9', 1, 13, '8', 1]
>>> lis.remove(1)
>>> print(lis)
[2, 3, 5, 6, '7', [11, 12], 10, 4, '9', 13, '8', 1]
>>>
```

### pop

该方法是根据指定索引删除元素，默认删除最后一个，***返回被删除的元素。***如果不存在，抛出`ValueError`异常。

```sh
>>> print(lis)
[2, 3, 5, 6, '7', [11, 12], 10, 4, '9', 13, '8', 1]
>>> lis.pop()
1
>>> print(lis)
[2, 3, 5, 6, '7', [11, 12], 10, 4, '9', 13, '8']
>>> lis.pop(0)
2
>>> print(lis)
[3, 5, 6, '7', [11, 12], 10, 4, '9', 13, '8']
>>>
```

### clear

删除list中的所有元素。返回一个空列表。

```sh
>>> print(lis)
[[1, 2], [3, 4], [5, 6]]
>>> lis.clear()
>>> print(lis)
[]
>>>
```

### sort

对列表进行排序。需注意：

- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，`reverse = True`降序，`reverse = False`升序（默认）。

```sh
>>> print(lis)
[4, 10, 13, 6, 5, 3]
>>> lis.sort()
>>> lis.sort(re)
repr(      return     reversed(  
>>> lis.sort(reverse=True)
>>> print(lis)
[13, 10, 6, 5, 4, 3]
```

带key的排序：

```sh
>>> lis = [[1, 2], [3, 4], [5, 6]]
>>> shuffle(lis)
>>> print(lis)
[[1, 2], [5, 6], [3, 4]]
>>> lis.sort(key=second_element)
>>> print(lis)
[[1, 2], [3, 4], [5, 6]]
>>>
```

### reverse

该方法将这个列表里的元素反转过来。

```shell
>>> print(lis2)
['8', 13, '9', 4, 10, [11, 12], '7', 6, 5, 3]
>>> lis2.reverse()
>>> print(lis2)
[3, 5, 6, '7', [11, 12], 10, 4, '9', 13, '8']
>>>
```

## del

删除列表中的元素。删除取到的元素。

```py
>>> lis = [1, 2, 3, 4]
>>> del lis[1:2]
>>> lis
[1, 3, 4]
>>> del lis[1]
>>> lis
[1, 4]
>>>
```
