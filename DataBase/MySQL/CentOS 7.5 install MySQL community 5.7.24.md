# CeotOS 7.5 install MySQL Community 5.7.24

CentOS 7.5的yum源已经替换掉了MySQL的，改用了Maria DB了。在CentOS 7.5 中安装MySql。

## 下载MySQL的repo

通过官网下载MySQL的repo，CentOS 7的[下载链接](https://repo.mysql.com//mysql80-community-release-el7-1.noarch.rpm),点击下载

**注：</br>**

- 这里下载的是8.0的版本，安装5.7需要重新配置。
  
## 安装yum源

安装下载好的repo文件

```shell
yum localinstall mysql80-community-release-el7-1.noarch.rpm
```

其中：把`mysql80-community-release-el7-1.noarch.rpm`换成相对应的包名。</br>
安装过程：

```shell
[root@localhost ~]# yum localinstall mysql80-community-release-el7-1.noarch.rpm
Loaded plugins: fastestmirror
Examining mysql80-community-release-el7-1.noarch.rpm: mysql80-community-release-el7-1.noarch
Marking mysql80-community-release-el7-1.noarch.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package mysql80-community-release.noarch 0:el7-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================
 Package                Arch   Version
                                     Repository                               Size
===================================================================================
Installing:
 mysql80-community-release
                        noarch el7-1 /mysql80-community-release-el7-1.noarch  31 k

Transaction Summary
===================================================================================
Install  1 Package

Total size: 31 k
Installed size: 31 k
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : mysql80-community-release-el7-1.noarch                          1/1
  Verifying  : mysql80-community-release-el7-1.noarch                          1/1

Installed:
  mysql80-community-release.noarch 0:el7-1

Complete!
```

### 验证是否安装成功

通过一下命令验证是否安装成功

```shell
yum repolist enabled | grep "mysql.*-community.*"
```

出现一下结果说明安装成功了。

```shell
[root@localhost ~]# yum repolist enabled | grep "mysql.*-community.*"
mysql-connectors-community/x86_64 MySQL Connectors Community                  74
mysql-tools-community/x86_64      MySQL Tools Community                       74
mysql80-community/x86_64          MySQL 8.0 Community Server                  49
```

***注意：***
安装成功之后需要更新yum，但是，官网介绍说，更新之后会替代其他的在yum源中的MySQL三方包

## 配置对应的MySQL的社区版本

### 通过yum-config-manager配置

如果系统支持`yum-config-manager`，则可以配置。

```shell
yum-config-manager --disable mysql57-community
yum-config-manager --enable mysql80-community
```

### 通过MySQL的yum配置文件配置

如果系统不支持`yum-config-manager`，则需要通过配置`/etc/yum.repos.d/mysql-community.repo`文件中的`enable`的值来完成:

- enable=1 ===> 使用当前版本
- enable=0 ===> 不适用当前版本

```shell
# Enable to use MySQL 5.7
[mysql57-community]
name=MySQL 5.7 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

[mysql80-community]
name=MySQL 8.0 Community Server
baseurl=http://repo.mysql.com/yum/mysql-8.0-community/el/7/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
```

修改后保存，然后查看允许使用的MySQL版本：

```shell
[root@localhost ~]# yum repolist enabled | grep mysql
mysql-connectors-community/x86_64 MySQL Connectors Community                  74
mysql-tools-community/x86_64      MySQL Tools Community                       74
mysql57-community/x86_64          MySQL 5.7 Community Server                 307
```

## 安装MySQL

配置完成`yum`后，通过`yum install mysql-community-server`命令来安装。其中：该命令自动安装的包有如下：

- MySQL server (mysql-community-server)
- MySQL client (mysql-community-client)
- The common error messages and character sets for client and server (mysql-community-common)
- The shared client libraries (mysql-community-libs).

```shell

```
