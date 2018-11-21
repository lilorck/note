# Git的初始化设置

Git安装成功之后的Git的初始化配置

## Git配置GitHub账户

安装完成之后要进行git的配置，这里配置的是GitHub账户

```shell
MisSa@DESKTOP-PIQ06QO MINGW64 /f
$ git config --global user.name RocsSun

MisSa@DESKTOP-PIQ06QO MINGW64 /f
$ git config --global user.email 710989028@qq.com
```

注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

创建仓库：
在F(Project)盘中创建一个新仓库mygitpro

```shell
MisSa@DESKTOP-PIQ06QO MINGW64 ~
$ cd f:

MisSa@DESKTOP-PIQ06QO MINGW64 /f
$ mkdir mygitpro

MisSa@DESKTOP-PIQ06QO MINGW64 /f
$ cd mygitpro/

MisSa@DESKTOP-PIQ06QO MINGW64 /f/mygitpro
$ git init
Initialized empty Git repository in F:/mygitpro/.git/

MisSa@DESKTOP-PIQ06QO MINGW64 /f/mygitpro (master)
$ ls -a
./  ../  .git/
```
