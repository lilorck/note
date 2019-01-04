# Anaconda3 安装报错 bunzip2: command not found

## 报错信息

```shell
Anaconda3-5.3.1-Linux-x86_64.sh: line 353: bunzip2: command not found
tar: This does not look like a tar archive
tar: Exiting with failure status due to previous errors
```

## 解决方法和原因

由于系统缺少`bunzip2`包造成的，通过yum安装`bzip2`包来解决

```shhell
yum install bzip2
```

## 分析和解决过程

可能是由于缺少`bunzip2`包导致的，先尝试安装这个包：

```shell
[root@localhost ~]# yum install bunzip2
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
No package bunzip2 available.
Error: Nothing to do
```

发现没找到这个包。百度下这个包：

> bunzip2，.bz2文件的解压缩程序。可解压缩.bz2格式的压缩文件。bunzip2实际上是bzip2的符号连接，执行`bunzip2`与`bzip2 -d`的效果相同

再次尝试`bzip2`包名

```shell
[root@localhost ~]# yum install bzip2
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
Resolving Dependencies
--> Running transaction check
---> Package bzip2.x86_64 0:1.0.6-13.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================
 Package          Arch              Version                  Repository       Size
===================================================================================
Installing:
 bzip2            x86_64            1.0.6-13.el7             base             52 k

Transaction Summary
===================================================================================
Install  1 Package

Total download size: 52 k
Installed size: 82 k
Is this ok [y/d/N]: y
Downloading packages:
bzip2-1.0.6-13.el7.x86_64.rpm                               |  52 kB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : bzip2-1.0.6-13.el7.x86_64                                       1/1
  Verifying  : bzip2-1.0.6-13.el7.x86_64                                       1/1

Installed:
  bzip2.x86_64 0:1.0.6-13.el7

Complete!
```

再次安装，没有报错，解决该错误。