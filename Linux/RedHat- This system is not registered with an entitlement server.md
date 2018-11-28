# 注册RedHat并使用RedHat的yum源

环境：

```shell
[root@localhost ~]# cat /etc/redhat-release 
Red Hat Enterprise Linux Server release 7.6 (Maipo)
```

## This system is not registered with an entitlement server

在虚拟机中安装好了RedHat之后使用yum更新，抛出一下信息;

```shell
Loaded plugins: product-id, search-disabled-repos, subscription-manager
This system is not registered with an entitlement server. You can use subscription-manager to register.
There are no enabled repos.
 Run "yum repolist all" to see the repos you have.
 To enable Red Hat Subscription Management repositories:
     subscription-manager repos --enable <repo>
 To enable custom repositories:
     yum-config-manager --enable <repo>
```

这个原因是因为没有在Redhat的服务器上注册该系统，需要我们使用`subscription-manager`命令注册。

## 注册系统

由于是通过订阅下载的RedHat，所以进行激活系统

> subscription-manager register

```shell
[root@localhost ~]# subscription-manager register
Registering to: subscription.rhsm.redhat.com:443/subscription
Username: rocsun
Password: 
The system has been registered with ID: 7847f407-f5ca-42bd-85d3-279a7f48046e
The registered system name is: localhost.localdomain
[root@localhost ~]# cat /etc/redhat-release 
Red Hat Enterprise Linux Server release 7.6 (Maipo)
```

## receiving is not updates

然后更新系统，发现注册了，但是还没有更新订阅。

```shell
[root@localhost ~]# yum update
Loaded plugins: product-id, search-disabled-repos, subscription-manager
This system is registered with an entitlement server, but is not receiving updates. You can use subscription-manager to assign subscriptions.
There are no enabled repos.
 Run "yum repolist all" to see the repos you have.
 To enable Red Hat Subscription Management repositories:
     subscription-manager repos --enable <repo>
 To enable custom repositories:
     yum-config-manager --enable <repo>
```

## 更新订阅

> subscription-manager attach --auto

```shell
[root@localhost ~]# subscription-manager attach --auto
Installed Product Current Status:
Product Name: Red Hat Enterprise Linux Server
Status:       Subscribed
```

至此，RedHat的注册和更新订阅完成，能够连接服务器更新系统以及使用RedHat的yum源。