# String

字符串或串(String)是由数字、字母、下划线组成的一串字符，是编程语言中表示文本的数据类型。由引号（'', ""）包括起来，记为:

```python
s="a1a2···an"(n>=0)
s1 = 'python'
```

**特点：**</br>

- str是不可变的数据类型
- str具有下标索引

## 冒号切割

python的字串列表有2种取值顺序:

1. 从左到右索引默认0开始的，最大范围是字符串长度少1
2. 从右到左索引默认-1开始的，最大范围是字符串开头
3. 取值时，从第一个元素起，默认是从左往右取，步长带负号`-`则会从右往左切，如果取不到，会返回空字符串。
4. `[头下标:尾下标:步长]`获取的子字符串包含头下标的字符，但不包含尾下标的字符，每次按步长来取，当前元素下标加步长，默认步长是‘1’。

切片代码：

```shell
Python 3.6.8 (default, Jan  4 2019, 20:23:10)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> s = "abcdefghijklmn"
>>> s[0::]
'abcdefghijklmn'
>>> s[0:4:]
'abcd'
>>> s[0:7:2]
'aceg'
>>> s[-1:-7:2]
''
>>> s[-7:-1:2]
'hjl'
>>> s[-7:-1:-2]
''
>>> s[-1:-7:-2]
'nlj'
>>> s
'abcdefghijklmn'
>>> s[-1::-1]
'nmlkjihgfedcba'
```

***当使用以冒号分隔的字符串，需注意：</br>***

- 每次切割返回一个新的对象。
- 包含左边的值，不包含右边的值

代码如下：

```python
>>> s1 = s[0:3]
>>> s2 = s[0:3]
>>> id(s1)
140661553654616
>>> id(s2)
140661553654504
>>> s1 is s2
False
>>> s = 'abcd'
>>> s[1:4]
'bcd'
>>> s[0:3]
'abc'
>>>
```

## 字符串的运算符

字符串的运算就是字符串的拼接，重复，以及判断等操作。

| 操作符 | 解释 |
| ----- | ----- |
| +    | 字符串连接 |
| \*   | 重复输出字符串 |
| []   | 通过索引获取字符串中字符 |
| [ : ] | 截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第3个字符的。|
| in | 成员运算符，判断字符串中是否包含给定的字符，返回True或者False |
| not in | 成员运算符，同`in` |
| r/R | 原始字符串，原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 |
| % |格式字符串，请看下一节内容。 |

## 字符串格式化

Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。

| 操作符 | 解释 |
| ----- | ----- |
| %c    | 格式化字符及其ASCII码 |
| %s    | 格式化字符串 |
| %d    | 格式化整数 |
| %u    | 格式化无符号整型 |
| %o    | 格式化无符号八进制数 |
| %x    | 格式化无符号十六进制数 |
| %X    | 格式化无符号十六进制数（大写）|
| %f    | 格式化浮点数字，可指定小数点后的精度 |
| %e    | 用科学计数法格式化浮点数 |
| %E    | 作用同%e，用科学计数法格式化浮点数 |
| %g    | %f和%e的简写 |
| %G    | %f 和 %E 的简写 |
| %p    | 用十六进制数格式化变量的地址 |

## 字符串的内建函数（方法）

字符串可调用的方法，共有40个：

- [capitalize](#capitalize)
- [lower](#lower)
- [casefold](#casefold)

### capitalize

该方法的将返回一个首字母大写，其余的小写的字符串。源码：

```python
def capitalize(self): # real signature unknown; restored from __doc__
    """
    S.capitalize() -> str

    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.
    """
    return ""
```

实例

```py
>>> s = "aAsSAS"
>>> s.capitalize()
'Aassas'
>>>
```

### lower

该方法的将返回一个所有字符小写的字符串。***lower()只对`ASCII`也就是`A-Z`有效，但是其它一些语言里面存在小写的情况就没办法了 ,适用于ASCII和中文***，源码：

```py
def casefold(self): # real signature unknown; restored from __doc__
    """
    S.casefold() -> str

    Return a version of S suitable for caseless comparisons.
    """
    return ""
```

实例：

```py
>>> s = "aAsSAS"
>>> s.lower()
'aassas'
>>>
```

### casefold

`casefold`方法和`lower`非常类似，都可以把字符串变成小写，对`Unicode`的时候用`casefold`，也就是说其他语言里存在小写的时候，调用该方法。源码：

```py
def casefold(self): # real signature unknown; restored from __doc__
    """
    S.casefold() -> str

    Return a version of S suitable for caseless comparisons.
    """
    return ""
```

实例：

```py
>>> s = 'ß'
>>> s.lower()
'ß'
>>> s.casefold()
'ss'
>>>
```

### upper

该方法的将返回一个所有字符大写的字符串，源码：

```py
def upper(self): # real signature unknown; restored from __doc__
    """
    S.upper() -> str

    Return a copy of S converted to uppercase.
    """
    return ""
```

实例：

```py
>>> s = "aAsSAS"
>>> s.upper()
'AASSAS'
>>>
```

### title

返回基于标题的s版本，即单词以标题大小写字符开头，所有剩余的大小写字符都有小写。源码：

```py
def title(self): # real signature unknown; restored from __doc__
    """
    S.title() -> str

    Return a titlecased version of S, i.e. words start with title case
    characters, all remaining cased characters have lower case.
    """
    return ""
```

实例：

```py
>>> s = "you raise me up"
>>> s.title()
'You Raise Me Up'
>>>
```

### count

该方法返回目标字符串在字符串中出现的次数，返回值是int类型，默认是遍历完整个字符串，源码：

```py
def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
    """
    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
    """
    return 0
```

实例：

```py
>>> ss = "asdfgasdfasdfafsdf"
>>> ss.count(a)
>>> ss.count("a")
4
>>> ss.count("a", 2)
3
>>> ss.count("a", 2, 10)
2
>>>
```

### counter

返回一个指定长度居中的字符串，***指定长度 = 字符串的长度 + 补位的长度***，其中，如果给定的长度小于字符串的长度，则返回的是原字符串，如果的大于字符串的长度，遵循先左后右的补位原则

```py
def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
    """
    S.center(width[, fillchar]) -> str

    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)
    """
    return ""
```

实例：

```py
>>> s = "RocSun"
>>> s.center(3)
'RocSun'
>>> s.center(7)
' RocSun'
>>> s.center(8)
' RocSun '
>>> s.center(8, "*")
'*RocSun*'
>>>
```