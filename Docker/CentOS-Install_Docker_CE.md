# 安装Docker-CE

docker-ce指的是docker community edit。即社区版本。</br>
centos下的docker-ce的安装方式：</br>

- repositories
- RPM packages
- conveniece script

## 配置环境

- Windows10
- VM workstation 15 Pro
- CentOS 7.5

## 系统要求

- ***CentOS 7.x***
- The centos-extras repository must be enabled. This repository is enabled by default, but if you have disabled it, you need to re-enable it.

## 卸载就的版本

如果安装了docker的旧版本，先卸载。旧版本的Docker的名是：`docker`和`docker-engine`，新版本的包名是：`docker-ce`

```shell
$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
```

## repositories方式

### 设置repositories

```shell
sudo yum install -y yum-utils \
     device-mapper-persistent-data \
     lvm2
```

### 设置成稳定的仓库

```shell
sudo yum-config-manager \
     --add-repo \
     https://download.docker.com/linux/centos/docker-ce.repo
```

### 可选项(允许测试版本)

```shell
sudo yum-config-manager --enable docker-ce-edge
sudo yum-config-manager --enable docker-ce-test
```

可使用disable命令关闭

***注：***
- test：测试版本
- edge：吃鸡版，稳定版前的两个版本

### 安装Docker

#### 安装最新版本

```shell
sudo yum install docker-ce
```

#### 安装制定的版本

查看可安装的版本

```shell
yum list docker-ce --showduplicates | sort -r
```

制定版本安装

```shell
sudo yum install docker-ce-<VERSION STRING>
```

## RPM包安装

### 下载rpm包

跳转至<a herf=' https://download.docker.com/linux/centos/7/x86_64/stable/Packages/'>稳定版</a>或者是<a herf=' https://download.docker.com/linux/centos/7/x86_64/edge/Packages/'>edge</a>页面下载相应的rpm包

### 安装Docker-ce

执行一下命令安装，将下面的/path/to更改为下载Docker包的路径。

```shell
sudo yum install /path/to/package.rpm
```

## 脚本安装

***注意事项：***

1. 脚本安装会自动读取系统的版本信息，并自动安装相关的依赖包
2. 脚本安装没有自定义设置
3. 需要root权限执行
4. 不能用于生产环境

从以下连接下载安装脚本。

- get.docker.com：最新版本
- test.docker.com：测试版本

使用以下命令下载并保持到本地，并使用root权限安装：

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## 启动docker

### 启动docker

```shell
sudo systemctl start docker
```

### 开机启动docker

```shell
sudo systemctl enable docker
```

### 启动doncker镜像

```shell
docker run server-name
```

## 卸载DOcker-CE

### 卸载Docker—CE包

```shell
sudo yum remove docker-ce
```

### 删除docker的镜像，容器等文档

```shell 
sudo rm -rf /var/lib/docker
```