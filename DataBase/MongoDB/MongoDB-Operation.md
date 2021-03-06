# MongoDB的初步使用

MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。 </br>
MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。 </br>

它和我们使用的关系型数据库最大的区别就是约束性,可以说文件型数据库几乎不存在约束性,理论上没有主外键约束,没有存储的数据类型约束等等

关系型数据库中有一个 "表" 的概念,有 "字段" 的概念,有 "数据条目" 的概念

MongoDB中也同样有以上的概念,但是名称发生了一些变化,严格意义上来说,两者的概念即为相似,但又有些出入。

***MongoDB的每个表(Collection)中存储的每条数据(Documents)都是一个一个的Json,Json中的每一个字段(Key)我们称之为:Field </br>
就此我们引出了三个关键字,Collection也就是关系型数据库中"表"的概念,Documents就是"数据条目",Field就是"字段"***

## MongoDB数据库的选择

### 创建或者使用数据库

> use.DatabaseName

```shell
use LuffyCity
```

如果该数据库不存在，则会创建并且使用，如果存在了，则切换到改数据库下。

> db：代表当前所使用的数据库，

### 创建或者使用collection

collection相当于关系型数据库中的table。

> db.collectionName

同数据库的使用和创建一样

## MongonDB的操作

### MongoDB的插入

MongoDB的插入数据的三个关键字：

> insert: 插入一条或者多条数据,需要带有允许插入多条的参数,这个方法目前官方已经不推荐 </br>
> insertOne：插入一条数据,官方推荐 </br>
> insertMany：插入多条数据,无需参数控制,官方推荐

```shell
db.Oldboy.insert({'name':'Roc', 'age':19})
db.Oldboy.insertOne({'name':'Linga', 'age': 19})
db.Oldboy.insertMany([{'name':'Master','age':18}, {'name':'Saya','age':20}])
```

### MongoDB的查找

MongoDB的查找关键字：

> find(条件):
> findOne(条件):findOne()无条件查找一条数据,默认当前Collection中的第一条数据

```shell
db.Oldboy.find({'name': 'Master'})
db.Oldboy.findOne({'name':'Roc'})
db.Oldboy.findOne()
```

### MongoDB的修改

MongoDB的更新关键字.({"条件"},{"关键字":{"修改内容"}})：

> update: 根据条件修改该条数据的内容, 这个方法目前官方已经不推荐 </br>
> updateOne: 根据条件修改一条数据的内容,如出现多条,只修改最靠前的数据 </br>
> updateMany: 根据条件修改所有数据的内容,多条修改

```shell
db.girl.updateOne({'age':18}, {$set:{'name':"Million"}},)
db.girl.updateMany({'age':18},{$set:{'gender': 'male'}})
```

### MongoDB的删除

MongoDB的删除关键字：

> remove({条件}): 删除满足条件的选项，

***如果无条件删除数据,这里要注意了,这是删除所有数据,清空Collection***