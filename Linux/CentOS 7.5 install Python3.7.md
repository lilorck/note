# CentOS 7.5 编译安装Python3.7

在CentO S上通过编译安装Python3.7，添加python3软链，并使用python3.

## 环境：

- win10
- vmware workstation 14
- centos 7 最小化安装
- root权限,所有操作都是在root用户下操作

## 安装依赖和yum更新

安装Python3.7的前期准备。

### yum更新

个人习惯，安装包之前会更新yum源。

```shell
yum update
```

### 安装依赖项

安装Python 3.7所需的依赖:

```shell
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make
```

## 下载Python

在官网下载所需版本，这里用的是3.7版本

```shell
wget https://www.python.org/ftp/3.7.0/Python-3.7.0.tgz
```

## 安装Python

通过解压，配置编译，编译安装等步骤完成

### 解压

下载好了之后在文件所在目录解压，

```shell
tar -xvf Python-3.7.0.tgz
```

### 配置编译

进入到解压的python的目录里面，使用`Python3.7.0/configure`文件进行配置

```shell
cd Python-3.7.0
```

配置编译的的路径

```shell
./configure --prefix=/usr/local/python3
```

**注：</br>**
**这里--prefix是指定编译安装的文件夹**

优化选项（可选）：</br>
执行完上一步后会提示执行以下的代码对Python解释器进行优化，

```shell
./configure --enable-optimizations
```

### 编译和安装：

```shell
make && make install
```

## 添加软连接

添加软链或者添加到环境变量，直接输入python3就可以使用了

```shell
ln -s /usr/local/bin/python3 python3
```