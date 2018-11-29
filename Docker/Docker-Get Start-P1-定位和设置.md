# 定位和设置

安装好docker之后，进行该部分的操作，主要是测试docker。

## 准备docker环境

### 测试Docker版本

1.使用`docker --version`查看版本

```shell
[root@bogon ~]# docker --version
Docker version 18.09.0, build 4d60db4
```

查看安装信息：

- docker info
- docker --version

```shell
[root@bogon ~]# docker info
Containers: 0
 Running: 0
 Paused: 0
 Stopped: 0
Images: 0
Server Version: 18.09.0
Storage Driver: overlay2
 Backing Filesystem: xfs
 Supports d_type: true
 Native Overlay Diff: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: bridge host macvlan null overlay
 Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: c4446665cb9c30056f4998ed953e6d4ff22c7c39
runc version: 4fc53a81fb7c994640722ac585fa9ca548971871
init version: fec3683
Security Options:
 seccomp
  Profile: default
Kernel Version: 3.10.0-862.el7.x86_64
Operating System: CentOS Linux 7 (Core)
OSType: linux
Architecture: x86_64
CPUs: 1
Total Memory: 974.6MiB
Name: bogon
ID: SP2X:WFNN:LLTH:MHRD:WOIR:BKQL:DWLS:QRQM:6HAB:IQHG:IESB:QOKO
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): false
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
 127.0.0.0/8
Registry Mirrors:
 http://f1361db2.m.daocloud.io/
Live Restore Enabled: false
Product License: Community Engine

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

### 测试安装

通过一个简单的docker镜像来测试docker

- docker run hello-world    ：执行docker镜像

```shell
[root@bogon ~]# docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
d1725b59e92d: Pull complete 
Digest: sha256:523e382ab1801f2a616239b1052bb7ee5a7cce6a06cfed27ccb93680eacad6ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

docker安装成功了。

查看docker下载的镜像：

- docker image ls

```shell
[root@bogon ~]# docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              4ab4c602aa5e        2 months ago        1.84kB
```

查看已存在的容器

- docker container ls       ：查看正在运行的容器
- docker container ls -aq   ：查看容器id
- docker container ls --all : 查看所有的容器，包括已经推出的

```shell
[root@bogon ~]# docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
[root@bogon ~]# docker container ls --all
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
b70159c28f20        hello-world         "/hello"            23 minutes ago      Exited (0) 23 minutes ago                       naughty_keldysh
79ca9b6dd7c0        hello-world         "/hello"            24 minutes ago      Exited (0) 24 minutes ago                       stoic_bassi
[root@bogon ~]# docker container ls -aq
b70159c28f20
79ca9b6dd7c0
```