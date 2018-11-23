# MySQL通过源码安装

通过mysql源码，把mysql安装到opt目录下

## 环境

Ubuntu 18.04.1 LTS <br>
mysql-community 5.7.24 

## 准备

安装依赖包和下载MySQLtar.gz版本

### 安装依赖库libiao

使用以下两条命令安装：

```
apt-cache search libaio
apt-get install libaio1
```
过程：

```
root@master-ThinkPad-E455 apt-cache search libaio
libaio-dev - Linux kernel AIO access library - development files
libaio1 - Linux kernel AIO access library - shared library
root@master-ThinkPad-E455 apt-get install libaio1
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

***yum的安装使用以下两条命令：***

```
yum search libaio
yum install libaio
```

### 下载MySQL安装包

这里下载的是mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz包

## 安装

### 解压安装包

由于是安装在/opt/mysql目录下，而tar解压只能在已存在的路径向下进行解压，故，先创建mysql目录

```
mkdir /opt/mysql
```

然后解压包：

```
root@master-ThinkPad-E455:/opt/mysql# tar -zxvf /home/master/Downloads/mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz
```

### 创建mysql用户和mysql用户组

创建mysql用户和mysql用户组，并把mysql用户添加到mysql组下

```
root@master-ThinkPad-E455:~# groupadd mysql  
root@master-ThinkPad-E455:~# useradd -r -g mysql mysql

```

### 创建软连和权限设置

在/usr/local目录下创建名为mysql的软连

```
root@master-ThinkPad-E455:/usr/local# ln -s /opt/mysql/mysql-5.7.24-linux-glibc2.12-x86_64 mysql
root@master-ThinkPad-E455:/usr/local# ls
bin  etc  games  include  lib  man  mysql  sbin  share  src
```

在mysql中创建mysql-files目录，并提升权限，改变用户及用户组

```
root@master-ThinkPad-E455:/usr/local/mysql# mkdir mysql-files
root@master-ThinkPad-E455:/usr/local/mysql# chown mysql:mysql mysql-files
root@master-ThinkPad-E455:/usr/local/mysql# chmod 750 mysql-files

```

### 安装

执行以下命令

```
shell> bin/mysqld --initialize --user=mysql 
shell> bin/mysql_ssl_rsa_setup              
shell> bin/mysqld_safe --user=mysql & # Next command is optional
```

过程：

```
root@master-ThinkPad-E455:/usr/local/mysql# bin/mysqld --initialize --user=mysql2018-11-10T06:31:07.136423Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
2018-11-10T06:31:08.740392Z 0 [Warning] InnoDB: New log files created, LSN=45790
2018-11-10T06:31:09.177392Z 0 [Warning] InnoDB: Creating foreign key constraint system tables.
2018-11-10T06:31:09.395556Z 0 [Warning] No existing UUID has been found, so we assume that this is the first time that this server has been started. Generating a new UUID: 35df8e02-e4b2-11e8-a9eb-ec0ec455e1e1.
2018-11-10T06:31:09.431030Z 0 [Warning] Gtid table is not ready to be used. Table 'mysql.gtid_executed' cannot be opened.
2018-11-10T06:31:09.433885Z 1 [Note] A temporary password is generated for root@localhost: Eqdz)tyuO0px
root@master-ThinkPad-E455:/usr/local/mysql# mysql

Command 'mysql' not found, but can be installed with:

apt install mysql-client-core-5.7   
apt install mariadb-client-core-10.1

root@master-ThinkPad-E455:/usr/local/mysql# bin/mysql_ssl_rsa_setup
Generating a 2048 bit RSA private key
..........................................+++
.....+++
writing new private key to 'ca-key.pem'
-----
Generating a 2048 bit RSA private key
............................................+++
..+++
writing new private key to 'server-key.pem'
-----
Generating a 2048 bit RSA private key
...+++
..........+++
writing new private key to 'client-key.pem'
-----
root@master-ThinkPad-E455:/usr/local/mysql# bin/mysqld_safe --user=mysql
Logging to '/usr/local/mysql/data/master-ThinkPad-E455.err'.
2018-11-10T06:34:14.362635Z mysqld_safe Starting mysqld daemon with databases from /usr/local/mysql/data

```