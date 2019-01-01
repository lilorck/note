# CentOS 7.5 reset root password

忘记root密码，重新设置root密码

开机时选择主版本的内核，然后按e键进入编辑模式 </br>
![Alternate text](../images/e064caf6-5d22-4ee5-ace5-0156c6d2b371.png)

修改如图选项：

- ro ===> rw
- 添加：`init=/sysroot/bin/sh`

![Alternate text](../images/71f8c5bd-cb7a-4839-bae2-bd5f35df3555.png)

然后按`Ctrl+X`进入单用户模式</br>
输入一下命令：

```shell
chroot /sysroot
passwd root
touch /.autorelabel
```

重启:

```shell
exit
reboot
```

如图：</br>
![Alternate text](../images/6bf8b426-a897-4e90-8c11-afeefb1d26fa.png)