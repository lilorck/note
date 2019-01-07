# bool值

布尔值即：“真”和“假”，Python中的写法是大写第一个字母，“`True`”，“`False`”，用于`if`、`while`条件判断布尔值的真假。

## 目录

- [对象的Bool值](#对象的Bool值)
  - [Bool值是False的内置对象](#Bool值是False的内置对象)
- [Bool运算](#Bool运算)

## 对象的Bool值

一个类中定义了`__bool__()`方法的返回值是`False`，或者是`__len__()`方法的返回值是`0`，则这个类实例化的对象的Bool值是`False`，否则将对象视为true。

### Bool值是False的内置对象

Python中内置Bool值为False的对象：

- 常量定义为false：None和False。
- 任何数值类型的零：0，0.0，0j，Decimal(0)， Fraction(0, 1)
- 空序列和集合：''，()，[]，{}，set()， range(0)

## Bool运算-`and`,`or`,`not`

`and`，`or`，`not`三者的运算优先级依次降低，遵循从左到右的运算顺序。运算值如下表：

| 操作 | 解释 | 注释 |
| ---- | ---- | ---- |
| x or y | 如果x为假，则为y，否则为 x | （1） |
| x and y | 如果x为假，则为x，否则为 y | （2） |
| not x | 如果x为假，则为True，否则为False | （3） |

***注释：***

1. 这是一个短路运算符，因此只有在第一个参数为false时才会计算第二个参数。
2. 这是一个短路运算符，因此只有在第一个参数为真时它才会计算第二个参数。
3. not优先级低于非布尔运算符，`not a == b`等价于`not (a == b)`。
