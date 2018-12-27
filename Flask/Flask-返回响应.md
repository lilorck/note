# Flask中的返回值

flask中的响应的三个关键字：

- return ：相当于Django中的HttpResponse
- render_templates ：相当于Django中的render
- redirect ： 相当于Django这的redirect

其中：

- return: 直接返回的字符串，在前端渲染在body中。
- reder_templates: 返回jinja2渲染的模板页面。
- redirect：重定向到新的url对应的函数以及页面。