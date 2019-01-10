# 字典

字典是另一种可变容器模型，且可存储任意类型对象。字典和列表一样，也可以进行嵌套。

字典的每个键值`key=>value`对用冒号`:`分割，每个键值对之间用逗号，分割，整个字典包括在花括号`{}`中

## key键

根据key来计算出一个内存地址，然后将`value`保存在这个地址中，这种算法被称为哈希算法（hash），而hash表是不连续的，因此不能切片，也决定了按照内部的哈希表保存的key-value值是无序的。这个是字典那只快的原因。

在dict中存储的key-value中的key都是可哈希的，即不可变的数据类型：
int，str，tuple

***键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。***

### 字典通过key键的操作

主要是通过key键拿值，查找，更新和删除操作。但是，如果key不存在时，会抛出`KeyError`的异常。

```py
>>> dic = {3: 110, 2: 'allen', (1,2): 'Hello', 'linga': ['miss', 'Saya'], 'Ture': {55:66}}
>>> dic[3]
110
>>> dic[(1, 2)] = 'World'
>>> dic
{3: 110, 2: 'allen', (1, 2): 'World', 'linga': ['miss', 'Saya'], 'Ture': {55: 66}}
>>> dic['1']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: '1'
>>> del dic[(1, 2)]
>>> dic
{3: 110, 2: 'allen', 'linga': ['miss', 'Saya'], 'Ture': {55: 66}}
>>> dic[3] = '3'
>>> dic
{3: '3', 2: 'allen', 'linga': ['miss', 'Saya'], 'Ture': {55: 66}}
>>> dic[4] = 'nice'
>>> dic
{3: '3', 2: 'allen', 'linga': ['miss', 'Saya'], 'Ture': {55: 66}, 4: 'nice'}
>>>
```

## 字典的内置方法

字典的内置方法如下：

- [get](#get)
- [keys]()
- [fromkeys]()
- [values]()
- [items]()
- [pop]()
- [popitem]()
- [clear]()
- [setdeault]()
- [copy]()
- [update]()

### get

该方法是通过key键获取value，如果key不存在，则返回`None`，通过`d=None`来设置返回值。如果存在，则返回value。源码：

```py
def get(self, k, d=None): # real signature unknown; restored from __doc__
    """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
    pass
```

实例：

```py
>>> dic
{3: '3', 2: 'allen', 'linga': ['miss', 'Saya'], 'Ture': {55: 66}, 4: 'nice'}
>>> dic.get(3)
'3'
>>> dic.get(3, 's')
'3'
>>> dic.get(9)
>>>
```

### keys

该方法是获取key值，返回一个含有key值得dict_view。源码：
