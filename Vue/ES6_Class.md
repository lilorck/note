ES6 引入了关键字class来定义一个类，constructor是构造方法，this代表实例对象。<br>
类之间通过extends继承，继承父类的所有属性和方法。<br>
super关键字，它代指父类的this对象，子类必须在constructor中调用super()方法，否则新建实例时会报错，因为子类没有自己的this对象。调用super()得到this，才能进行修改。

```
<script>
    class Base{
        constructor(){
            this.type = 'Base';
        };
        test(args){
            console.log(this.type);
            console.log(args);
        }
    }

    class Ext extends Base{
        constructor(){
            super();
            this.type = 'Ext';
        };
    }
    
    let b = new Base();
    let e = new Ext();
</script>
```

