# 配置Docker云加速器

## 自动配置加速器

```shell
sudo curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
```
执行完上边的命令后重启docker

```shell
systemctl restart docker
```

## 手动配置加速器

查看docker版本：

> docker version

```shell
[root@bogon ~]# docker version
Client:
 Version:           18.09.0
 API version:       1.39
 Go version:        go1.10.4
 Git commit:        4d60db4
 Built:             Wed Nov  7 00:48:22 2018
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.0
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.4
  Git commit:       4d60db4
  Built:            Wed Nov  7 00:19:08 2018
  OS/Arch:          linux/amd64
  Experimental:     false
```

**Docker 版本在 1.12 或更高** </br>
创建或修改 /etc/docker/daemon.json 文件，修改为如下形式

```json
{
    "registry-mirrors": [
        "加速地址"
    ],
    "insecure-registries": []
}
```

其他版本请参照<a href="http://guide.daocloud.io/dcs/daocloud-9153151.html ">教程官网</a>配置