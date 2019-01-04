# CentOS 7.5 安装Anaconda 3

## 下载

这里下载的是清华源上的Anaconda3，[点击下载](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh)</br>

```shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh
```

## 依赖

会依赖`bunzip2`的解药工具，通过yum安装，yum安装的包名是：`bzip2`

```shell
yum install bzip2
```

## 安装

```shell
bash Anaconda3-5.3.1-Linux-x86_64.sh
```

提示阅读授权

```shell
[root@localhost ~]# bash Anaconda3-5.3.1-Linux-x86_64.sh
WARNING: bzip2 does not appear to be installed this may cause problems below

Welcome to Anaconda3 5.3.1

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>>
```

然后是确实是否同意授权

```shell
Do you accept the license terms? [yes|no]
[no] >>> yes
```

设置安装路径，默认在`/root/anaconda3`下边

```shell
Anaconda3 will now be installed into this location:
/root/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/root/anaconda3] >>>
```

这里需要制定安装的路径，然后开始安装

```shell
[/root/anaconda3] >>> /opt/anaconda3
PREFIX=/opt/anaconda3
installing: python-3.7.0-hc3d631a_0 ...
Python 3.7.0
installing: blas-1.0-mkl ...
...
installation finished.
```

接下来会提示是否添加到root的`.bashrc`中,默认`Enter`是`no`,回车

```shell
Do you wish the installer to initialize Anaconda3
in your /root/.bashrc ? [yes|no]
[no] >>>

You may wish to edit your /root/.bashrc to setup Anaconda3:

source /opt/anaconda3/etc/profile.d/conda.sh

Thank you for installing Anaconda3!
```

这里提示是否安装VSCode：

```shell
===========================================================================

Anaconda is partnered with Microsoft! Microsoft VSCode is a streamlined
code editor with support for development operations like debugging, task
running and version control.

To install Visual Studio Code, you will need:
  - Administrator Privileges
  - Internet connectivity

Visual Studio Code License: https://code.visualstudio.com/license

Do you wish to proceed with the installation of Microsoft VSCode? [yes|no]
>>> no
```

## 手动设置环境变量

手动将`export PATH=/opt/modules/anaconda3/bin:$PATH`添加到`/etc/profile`中</br>
最后`source /etc/profile`使环境变量生效