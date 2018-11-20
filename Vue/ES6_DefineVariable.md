# 变量的声明

ES6中声明变量的关键字:`var, const, let` <br>
var: 提升变量到当前命名空间的顶部，全局的变量提升到全局命名空间的顶部，函数内部的变量则提升到该层函数命名空间的顶部 <br>
const: 定义常量，定义之后不能修改 <br>
let: 定义变量，但是不存在变量的提升，以及是一个块级的变量，出了`{}`之后不能使用，且在必须是先定义，后使用，否则会报错。 <br>

```
<!DOCTYPE html>
<html lang="zh_CN">
<head>
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Page Title</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<script src="https://cdn.jsdelivr.net/npm/vue"></script>
</head>
<body>
	
	<script>

		const const_a = "const_a"
		console.log(const_a)
		// const const_a = "const_aa"
		// console.log(const_a)

		console.log(variable)
		var variable = "123"
		console.log(variable)

		{
			let let_a = '222'
			console.log(let_a)
			console.log(let_b)
			let let_b = '333'
		}

		console.log(let_b)
	</script>
</body>
</html>
```
GoogleChrome中的结果：
```
const_a
undefined
123
222
Uncaught ReferenceError: let_b is not defined at test.html:24
const_a = 1
VM267:1 Uncaught TypeError: Assignment to constant variable.
    at <anonymous>:1:9
variable = 1
1
```
