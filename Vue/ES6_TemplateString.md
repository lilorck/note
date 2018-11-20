# ES6模板字符串

样子: `` 反引号，tab上面的那个键，同该符号包裹的字符串能够带来的功能如下：

1.可以包涵换行 <br>
&#8194;&#8194;&#8194;&#8194;&#8194;在反引号以内，可以有多个换行，都能够在使用的时候被识别 <br>
2.可以嵌入变量 <br>
&ensp;&ensp;&ensp;&ensp;&ensp;使用美元符号和大括号包裹变量${对象名.属性名} <br>
3.可以原生输出 <br>
&#8194;&#8194;&#8194;&#8194;&#8194;原生输出包含转义字符串的内容String.raw模板字符串 <br>
例子：
```
<!DOCTYPE html>
<html lang="zh_CN">
<head>
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>function</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

	<div id="box">

	</div>
	
	<script>
		var obj = document.getElementById('box');
		var divBox = `
			<div>
				<h1>InnerBox</h1>
			</div>
		`;
		console.log(obj);
		obj.innerHTML = divBox;

		var a = 1;
		var b = 2;
		console.log(
			`result: ${ a + b }, ${ a*b}`
		)
	</script>

</body>
</html>
```