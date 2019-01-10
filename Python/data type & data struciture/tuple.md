# 元组

元组是只读列表，值能读，不能修改，但是元组嵌套了其他可变数据类型，可则已修改元组里的可变类型的数据。

```py
>>> tup = (1, 2, [3, 4], 5)
>>> tup[2].append(6)
>>> tup
(1, 2, [3, 4, 6], 5)
>>> tup[1] = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

元组由`()`表示，当只有一个元素是，后边要跟`,`括号也可以省虐不写。

```py
>>> t = 1,
>>> type(t)
<class 'tuple'>
>>>
```

## 元组的内置方法

元组的内置方法有两个，`count()`和`index()`两个。

### count

用于计数。同列表的用法，源码：

```py
def count(self, value): # real signature unknown; restored from __doc__
    """ T.count(value) -> integer -- return number of occurrences of value """
    return 0
```

### index

用于索引，同list的用法。源码：

```py
def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
    """
    T.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
    """
    return 0
```