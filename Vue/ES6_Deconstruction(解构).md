ES6中的数据解构和python中的`**, *`的作用一样，那数据打散，赋值给变量 <br>
列子：
```
<script>
    const dict = {
        name : 11,
        age : 22,
    };

    const lol = ['Ahro', 'Timo'];

    const {name, age} = dict;
    console.log(name);
    console.log(age);
    const [names, hero] = lol;
    console.log(names);
    console.log(hero);
</script>
```

***需注意的是字典要用字典去接，列表要用列表去接***