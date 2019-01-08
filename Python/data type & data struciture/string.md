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

### swapcase

该方法是返回一个交换大小写的字符串，源码：

```py
def swapcase(self): # real signature unknown; restored from __doc__
    """
    S.swapcase() -> str

    Return a copy of S with uppercase characters converted to lowercase
    and vice versa.
    """
    return ""
```

实例：

```py
>>> s = "RocSun"
>>> s.swapcase()
'rOCsUN'
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

### index

该方法返回就近匹配到的目标字符串的索引。默认遍历整个字符串，也可以指定起始索引。源码：

```py
def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
    """
    S.index(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Raises ValueError when the substring is not found.
    """
    return 0
```

实例：

```py
>>> s = 'Hello World!'
>>> s.index("l")
2
>>>
```

### find

该方法同index方法，源码：

```py
def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
    """
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
    """
    return 0
```

实例：

```py
>>> s = 'Hello World!'
>>> s.find("l")
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

### expandtabs

此方法返回在修改长度后的制表符（`\t`），默认值`tabsize=8`，修改应该是4的倍数，扩展后的制表符通过空格填充。***从效果来看，换成8个后和原始的效果一样。***源码：

```py
def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
    """
    S.expandtabs(tabsize=8) -> str

    Return a copy of S where all tab characters are expanded using spaces.
    If tabsize is not given, a tab size of 8 characters is assumed.
    """
    return ""
```

实例：

```py
>>> s = "Roc\tSun"
>>> print(s)
Roc	Sun
>>> print(s.expandtabs())
Roc     Sun
>>> print(s.expandtabs(12))
Roc         Sun
>>> print(s.expandtabs(16))
Roc             Sun
>>>
```

### split

该方法返回一个列表，传入切割字符，但是切割后的list中没有传入的切割字符。**默认的切割符是空格**，`sep=None`是切割字符， `maxsplit=-1`是切割次数，默认全部切割，**从左往右切割**。源码：

```py
def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
    """
    S.split(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are
    removed from the result.
    """
    return []
```

实例：

```py
>>> s = " Roc Sun "
>>> s.split()
['Roc', 'Sun']
>>> s.split("u")
[' Roc S', 'n ']
>>> s.split(" ", 1)
['', 'Roc Sun ']
>>>
```

### lsplit

该方法同`splite`方法，从右开始切割。源码：

```py
def rsplit(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
    """
    S.rsplit(sep=None, maxsplit=-1) -> list of strings

    Return a list of the words in S, using sep as the
    delimiter string, starting at the end of the string and
    working to the front.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified, any whitespace string
    is a separator.
    """
    return []
```

### splitlines

按行切割，默认是换行符

### strip

用来去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)，返回值是字符串。

- 参数chars是可选的，当chars为空，默认删除string头尾的空白符(包括\n、\r、\t、' ')
- 当chars不为空时，函数会被chars解成一个个的字符，然后将这些字符去掉。
- 字符串中间的不能删除

源码：

```py
def strip(self, chars=None): # real signature unknown; restored from __doc__
    """
    S.strip([chars]) -> str

    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    """
    return ""
```

实例：

```py
>>>  s = " Roc Sun "
>>> s.strip()
'Roc Sun'
>>> s.strip("u")
' Roc Sun '
>>> s1 = 'abcdfghsdba'
>>> s1.strip("ab")
'cdfghsd'
>>>
```

### lstrip

删除字符串左边的，同`strip`

### rstrip

删除字符串右边的，同`strip`

### join

该方法的返回值是字符串,传入一个可迭代对象通过指定的字符连接起来。源码：

```py
def strip(self, chars=None): # real signature unknown; restored from __doc__
    """
    S.strip([chars]) -> str

    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    """
    return ""
```

实例：

```py
>>> l = ['hey', 'baby', 'what', 'are', 'you', 'doing']
>>> ''.join(l)
'heybabywhatareyoudoing'
>>> t = tuple(l)
>>> print(t)
('hey', 'baby', 'what', 'are', 'you', 'doing')
>>> " ".join(t)
'hey baby what are you doing'
>>>
```

### replace

该方法返回一个替换后的字符串，传入要替换的字符，和目标字符，可选参数：替换次数，默认是全部替换掉，传入替换次数，从左往右替换x个。源码：

```py
def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
    """
    S.replace(old, new[, count]) -> str

    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.
    """
    return ""
```

实例：

```py
>>> s = "abcdabcdabcd"
>>> s.replace('a', 'o')
'obcdobcdobcd'
>>> s.replace('a', 'o', 1)
'obcdabcdabcd'
>>>
```

### encode

返回一个指定编码格式的bytes类型。源码：

```py
def encode(self, encoding='utf-8', errors='strict'): # real signature unknown; restored from __doc__
    """
    S.encode(encoding='utf-8', errors='strict') -> bytes

    Encode S using the codec registered for encoding. Default encoding
    is 'utf-8'. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.
    """
    return b""
```

实例：

```py
>>> s = "abcdabcdabcd"
>>> s.encode('utf8')
b'abcdabcdabcd'
>>> s.encode('GBK')
b'abcdabcdabcd'
>>> s1 = s.encode('gbk')
>>> type(s1)
<class 'bytes'>
>>>
```

### startswith

判断是否以目标字符开始的，返回值是boolean。传入指定的字符或者子字符，可以使用元组，会解构逐一匹配。`start=None`和`end=None`指定检测区间,***这个区间的特点是左闭右开区间***。源码：

```py
def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
    """
    S.startswith(prefix[, start[, end]]) -> bool

    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.
    """
    return False
```

实例：

```py
>>> s2 = 'abcd'
>>> s2.startswith('a')
True
>>> s2.startswith(('c',) , 2, 3)
True
>>> s2.startswith(('c', 'd') , 1, 2)
False
>>> s2.startswith(('b','c',) , 2, 3)
True
>>> s2.startswith(('a','c',) , 2, 3)
True
>>>
```

### endswith

判断是否以目标字符结束的，方法同`startswith`。源码：

```py
def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
    """
    S.endswith(suffix[, start[, end]]) -> bool

    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.
    """
    return False
```

```py
>>> s2 = 'abcd'
>>> s2.endswith('d')
True
>>> s2.endswith('d', 2, 3)
False
>>> s2.endswith('d', 2, 4)
True
>>>
```

### format

该方法用于字符串的格式化输出。它通过{}和:来代替传统%方式。传值方式：

- 使用位置参数：位置参数不受顺序约束，且可以为{},只要format里有相对应的参数值即可,参数索引从0开，传入位置参数列表可用*列表
- 使用关键字参数：关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可。

源码:

```py
def format(self, *args, **kwargs): # known special case of str.format
    """
    S.format(*args, **kwargs) -> str

    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').
    """
    pass
```

实例：

```py

```