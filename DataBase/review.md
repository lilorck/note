# 数据库复习

## 面试点：

1. 表的设计
2. SQL查询
3. 存储引擎
   1. 事务
4. 索引
   1. 作用
      1. 加速查找
      2. 约束
   2. 种类：
      1. 主键索引：
         - 不能为空
         - 不能重复
      2. 唯一索引
         - 不能重复  
      3. 普通索引
      4. 联合索引
      5. 联合唯一索引
         1. 联合唯一
         2. 联合索引是，如果要命中索引。必须遵循“最左前缀原则”
      6. 覆盖索引
         1. 在索引的
      7. 索引合并
5. 数据库的优化
   1. 分库
      1. 大库分成多个小库
   2. 分表
      1. 垂直分表
      2. 水平分表
   3. 读写分离
   4. 