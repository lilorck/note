# 访问请求数据

在Flask中,客户端发送给服务器的数据交互由全局的`request`对象来提供这些信息。Flask中保证线程安全是通过**“环境作用域”**实现的

## 环境局部变量

官方解释：

> Flask 中的某些对象是全局对象，但却不是通常的那种。这些对象实际上是特定环境的局部对象的代理。虽然很拗口，但实际上很容易理解。

绑定

> 想象一下处理线程的环境。一个请求传入，Web 服务器决定生成一个新线程（ 或者别的什么东西，只要这个底层的对象可以胜任并发系统，而不仅仅是线程）。 当 Flask 开始它内部的请求处理时，它认定当前线程是活动的环境，并绑定当前的应用和 WSGI 环境到那个环境上（线程）。它的实现很巧妙，能保证一个应用调用另一个应用时不会出现问题。</br>
> </br>
> 所以，这对你来说意味着什么？除非你要做类似单元测试的东西，否则你基本上可以完全无视它。你会发现依赖于一段请求对象的代码，因没有请求对象无法正常运行。解决方案是，自行创建一个请求对象并且把它绑定到环境中。单元测试的最简单的解决方案是：用 test_request_context() 环境管理器。结合 with 声明，绑定一个测试请求，这样你才能与之交互。下面是一个例子:

```python
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
```

另一种可能是：传递整个 WSGI 环境给 request_context() 方法:

```python
from flask import request

with app.request_context(environ):
    assert request.method == 'POST'
```
