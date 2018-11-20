# 环境

Windows 10 <br> 
VMware Workstation Pro 15 <br>
CentOS 7.5 <br>

# 过程

安装搭建好了编译环境后，进行configure配置检查：
```
configure:3476: checking for --without-gcc
configure:3499: result: no
configure:3502: checking for --with-icc
configure:3522: result: no
configure:3646: checking for gcc
configure:3676: result: no
configure:3739: checking for cc
configure:3786: result: no
configure:3842: checking for cl.exe
configure:3872: result: no
configure:3896: error: in `/home/roc/Python-3.6.7':
configure:3898: error: no acceptable C compiler found in $PATH
See `config.log' for more details
```

这里提示缺少C编译器，安装gcc编译器：

```
sudo yum  install gcc
```






优化选项


If you want a release build with all stable optimizations active (PGO, etc),
please run ./configure --enable-optimizations

http://nginx.org/download/nginx-1.14.0.tar.gz

http://nginx.org/download/nginx-1.12.2.tar.gz