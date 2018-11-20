#### 环境

Windows 10

python 3.6.7

#### 安装virtualenv

virtualenv用于创建虚拟环境，用于隔离不同的python版本的运行，是容器类软件。这里在Windows下通过pip安装：

```
pip install virtualenv
```

#### 创建虚拟环境

创建虚拟环境是通过virtualenv的命令直接创建，一般是需要制定参数的：

```
virtualenv --no-site-packages -p C:\Python36\python.exe venv
# --no-site-packages 这里是新的虚拟环境不能访问全局的site-packages
# -p 指定使用的python解释器
# venv 当前路径下创建虚拟环境venv
```

#### 启动和关闭虚拟环境

启动虚拟环境时，要注意的是启动时要先要进入虚拟环境venv下的Scripts文件夹下，执行activate文件

```
F:\venv>cd Scripts

F:\venv\Scripts>activate

(venv) F:\venv\Scripts>
```

***一定要使用cmd！！！powershell跑不起来***

```
***powershell坑爹的地方在于执行activate.bat脚本之后不会尸体"(venv)"，这是坑爹的地方！！！***
```

关闭虚拟环境是在使用虚拟环境的任何地方直接使用deactivate退出虚拟环境。

```
(venv) F:\venv\Scripts>deactivate
F:\venv\Scripts>
```

#### virtualenv的用法和参数

##### virtualenv的用法：

```
virtualenv [OPTIONS] DEST_DIR
```

##### virtualenv的参数：

```
--version
显示当前版本号。
-h, --help
显示帮助信息。
-v, --verbose
显示详细信息。
-q, --quiet
不显示详细信息。
-p PYTHON_EXE, --python=PYTHON_EXE
指定所用的python解析器的版本，比如 --python=python2.5 就使用2.5版本的解析器创建新的隔离环境。 默认使用的是当前系统安装(/usr/bin/python)的python解析器
--clear
清空非root用户的安装，并重头开始创建隔离环境。
--no-site-packages
令隔离环境不能访问系统全局的site-packages目录。
--system-site-packages
令隔离环境可以访问系统全局的site-packages目录。
--unzip-setuptools
安装时解压Setuptools或Distribute
--relocatable
重定位某个已存在的隔离环境。使用该选项将修正脚本并令所有.pth文件使用相当路径。
--distribute
使用Distribute代替Setuptools，也可设置环境变量VIRTUALENV_DISTRIBUTE达到同样效要。
--extra-search-dir=SEARCH_DIRS
用于查找setuptools/distribute/pip发布包的目录。可以添加任意数量的–extra-search-dir路径。
--never-download
禁止从网上下载任何数据。此时，如果在本地搜索发布包失败，virtualenv就会报错。
--prompt==PROMPT
定义隔离环境的命令行前缀。
```
