# 安装libaio包

安装MySQL是缺少这个包， 使用apt进行安装

```
root@master-ThinkPad-E455:/usr/bin/mysql/bin# apt install libaio
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package libaio
```

宝错了，使用apt-get

```
root@master-ThinkPad-E455:/usr/bin/mysql/bin# apt-get install libaio
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package libaio
```

## 报错原因

包名错误导致的，在apt中的包名是`libaio1`

## 解决方法

使用以下命令安装

```
apt-cache search libaio
apt-get install libaio1
```

过程：

```
master@master-ThinkPad-E455:~$ sudo apt-cache search libaio
libaio-dev - Linux kernel AIO access library - development files
libaio1 - Linux kernel AIO access library - shared library
master@master-ThinkPad-E455:~$ sudo apt-get install libaio1
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  libaio1
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 6,448 B of archives.
After this operation, 30.7 kB of additional disk space will be used.
Get:1 http://cn.archive.ubuntu.com/ubuntu bionic/main amd64 libaio1 amd64 0.3.110-5 [6,448 B]
Fetched 6,448 B in 2s (3,138 B/s)  
Selecting previously unselected package libaio1:amd64.
(Reading database ... 165761 files and directories currently installed.)
Preparing to unpack .../libaio1_0.3.110-5_amd64.deb ...
Unpacking libaio1:amd64 (0.3.110-5) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Setting up libaio1:amd64 (0.3.110-5) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...

```