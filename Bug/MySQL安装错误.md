# MySQL安装报错

```bush
[root@localhost ~]# yum install mysql-server
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
Resolving Dependencies
--> Running transaction check
---> Package mysql-community-server.x86_64 0:5.7.24-1.el7 will be installed
--> Processing Dependency: mysql-community-common(x86-64) = 5.7.24-1.el7 for package: mysql-community-server-5.7.24-1.el7.x86_64
--> Processing Dependency: mysql-community-client(x86-64) >= 5.7.9 for package: mysql-community-server-5.7.24-1.el7.x86_64
--> Processing Dependency: net-tools for package: mysql-community-server-5.7.24-1.el7.x86_64
--> Running transaction check
---> Package mysql-community-client.x86_64 0:5.7.24-1.el7 will be installed
---> Package mysql-community-server.x86_64 0:5.7.24-1.el7 will be installed
--> Processing Dependency: mysql-community-common(x86-64) = 5.7.24-1.el7 for package: mysql-community-server-5.7.24-1.el7.x86_64
---> Package net-tools.x86_64 0:2.0-0.24.20131004git.el7 will be installed
--> Finished Dependency Resolution
Error: Package: mysql-community-server-5.7.24-1.el7.x86_64 (mysql57-community)
           Requires: mysql-community-common(x86-64) = 5.7.24-1.el7
           Installed: mysql-community-common-8.0.13-1.el7.x86_64 (@mysql80-community)
               mysql-community-common(x86-64) = 8.0.13-1.el7
           Available: mysql-community-common-5.7.9-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.9-1.el7
           Available: mysql-community-common-5.7.10-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.10-1.el7
           Available: mysql-community-common-5.7.11-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.11-1.el7
           Available: mysql-community-common-5.7.12-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.12-1.el7
           Available: mysql-community-common-5.7.13-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.13-1.el7
           Available: mysql-community-common-5.7.14-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.14-1.el7
           Available: mysql-community-common-5.7.15-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.15-1.el7
           Available: mysql-community-common-5.7.16-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.16-1.el7
           Available: mysql-community-common-5.7.17-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.17-1.el7
           Available: mysql-community-common-5.7.18-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.18-1.el7
           Available: mysql-community-common-5.7.19-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.19-1.el7
           Available: mysql-community-common-5.7.20-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.20-1.el7
           Available: mysql-community-common-5.7.21-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.21-1.el7
           Available: mysql-community-common-5.7.22-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.22-1.el7
           Available: mysql-community-common-5.7.23-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.23-1.el7
           Available: mysql-community-common-5.7.24-1.el7.x86_64 (mysql57-community)
               mysql-community-common(x86-64) = 5.7.24-1.el7
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
```