# Git连接GitHub

记录Git连接至GitHub的过程

## 配置Git用户和邮箱

配置git全局用户和邮箱，连接GitHub的话要配置成GitHub的用户名和邮箱，但是下边我用的不是GitHub的用户名，也能够用。</br>

- git config --global user.name username
- git config --global user.name email_address

```dos
Roc@DESKTOP-AF552U2 MINGW64 /f/mygitpro
$ git config --global user.name RocSun

Roc@DESKTOP-AF552U2 MINGW64 /f/mygitpro
$ git config --global user.email 710989028@qq.com
```

## 创建SSH密匙对

推送至GitHub时需要用到SSH密匙对，通过git制作密钥对，Windows下的密钥保存在`C:\User\UserName\.ssh`文件夹下边，一个公钥`id_rsa.pub`文件，一个私钥`id_rsa`文件。后边的邮箱是GitHub的邮箱，是否需要密码看心情。

- ssh-keygen -t rsa -C '注册GitHub的邮箱'

```dos
Roc@DESKTOP-AF552U2 MINGW64 /f/mygitpro (master)
$ ssh-keygen -t rsa -C '710989028@qq.com'
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/Roc/.ssh/id_rsa):
Created directory '/c/Users/Roc/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/Roc/.ssh/id_rsa.
Your public key has been saved in /c/Users/Roc/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:s9KZlaSzp3qlmY/u/nEpxOIpRwV04CNY7WFcpIPxUBE 710989028@qq.com
The key's randomart image is:
+---[RSA 2048]----+
|      +=E*+      |
|     o *=+       |
|    . oo*.o      |
|       ..B .     |
|        S =      |
|       + %.  .   |
|      o X=+ o    |
|       +=+ +     |
|      .**oo      |
+----[SHA256]-----+
```

ssh创建成功，在GitHub上添加SSH后进行测试。

- ssh -T git@github.com

```dos
Roc@DESKTOP-AF552U2 MINGW64 ~
$ ssh -T git@github.com
The authenticity of host 'github.com (13.229.188.59)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,13.229.188.59' (RSA) to the list of known hosts.
Hi RocsSun! You've successfully authenticated, but GitHub does not provide shell access.
```

## 初始化仓库

将目标文件夹初始化仓库

- git init

```dos
Roc@DESKTOP-AF552U2 MINGW64 /e/note
$ ls
 Bug/            Flask/        MySQL/     python安装报错.md      Vue/
 Django/         Git/          Project/   Redis/                 孙鹏飞.md
 Django回顾.md   JavaScript/   Python/   'Virtualenv&wrapper'/

Roc@DESKTOP-AF552U2 MINGW64 /e/note
$ git init
Initialized empty Git repository in E:/note/.git/
```

## 添加到仓库，并提交到仓库

将目标文件添加到仓库，并提交到仓库

- git add file
- git commit -m 'message'

```dos
Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git add ./*

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git commit -m '初始化仓库，提交以前的所有笔记'
[master (root-commit) 53ab25a] 初始化仓库，提交以前的所有笔记
 39 files changed, 2260 insertions(+)
 create mode 100644 Bug/Windows-0x80070570.md
 create mode 100644 "Bug/python\345\256\211\350\243\205\346\212\245\351\224\231.md"
 create mode 100644 "Bug/\346\225\260\346\215\256\350\277\201\347\247\273\346\212\245\351\224\231.md"
 create mode 100644 Django/Django-module/Django-Admin.md
 create mode 100644 Django/Django-module/Django-Form&ModelForm.md
 create mode 100644 Django/Django-module/Django-Meta.md
 create mode 100644 Django/Django-module/Django-field.py
 create mode 100644 Django/Django-module/HTTP.md
 create mode 100644 Django/Django-module/MVC.md
 create mode 100644 Django/Django-module/MVT.md
 create mode 100644 Django/Django-rest-framework/Django-rest-framework-Install.md
 create mode 100644 Django/Django-rest-framework/Django-rest-framework-Serializers.md
 create mode 100644 Django/Django-rest-framework/Django-rest-framwork-startquickly.md
 create mode 100644 "Django\345\233\236\351\241\276.md"
 create mode 100644 "Flask/flask\347\232\204\345\256\211\350\243\205\345\217\212\345\277\253\351\200\237\350\277\220\350\241\214.md"
 create mode 100644 "Git/git\347\232\204\345\210\235\346\254\241\344\275\277\347\224\250.md"
 create mode 100644 "Git/git\347\232\204\351\200\211\351\241\271\345\217\202\346\225\260.md"
 create mode 100644 Project/BBS/BBS_database_design.md
 create mode 100644 Project/blog/blog_database.md
 create mode 100644 Python/meriyouxian.py
 create mode 100644 "Redis/Redis\347\232\204\344\273\213\347\273\215.md"
 create mode 100644 Virtualenv&wrapper/Virtualenvwrapper.md
 create mode 100644 "Virtualenv&wrapper/virtualenv\347\232\204\344\275\277\347\224\250.md"
 create mode 100644 Vue/ES6_Class.md
 create mode 100644 "Vue/ES6_Deconstruction(\350\247\243\346\236\204).md"
 create mode 100644 Vue/ES6_DefineVariable.md
 create mode 100644 Vue/ES6_ImportExport.md
 create mode 100644 Vue/ES6_TemplateString.md
 create mode 100644 "Vue/Vue-\347\273\204\345\273\272.md"
 create mode 100644 "Vue/Vue_\346\214\207\344\273\244.md"
 create mode 100644 "Vue/Vue\345\277\203\345\276\227.md"
 create mode 100644 "Vue/Vue\347\232\204\345\237\272\347\241\200\346\223\215\344\275\234.md"
 create mode 100644 Vue/luffy.html
 create mode 100644 Vue/routelink.html
 create mode 100644 Vue/test.html
 create mode 100644 Vue/vue.html
 create mode 100644 "Vue/\347\273\204\345\273\272.html"
 create mode 100644 "python\345\256\211\350\243\205\346\212\245\351\224\231.md"
 create mode 100644 "\345\255\231\351\271\217\351\243\236.md"
```

## 关联远程仓库

在GitHub上新建一个空仓库，并使用git关联GitHub的新建仓库。

- git remote add origin git@github.com:GitHubName/RepositoryName.git

```dos
Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git remote add origin git@github.com:RocsSun/note.git
```

## 推送至GitHub仓库

第一次推送要使用`-u`选项。

- git push -u origin master

```dos
Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git push -u origin master
Enumerating objects: 49, done.
Counting objects: 100% (49/49), done.
Delta compression using up to 4 threads
Compressing objects: 100% (43/43), done.
Writing objects: 100% (49/49), 32.97 KiB | 1.14 MiB/s, done.
Total 49 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/RocsSun/note/pull/new/master
remote:
To github.com:RocsSun/note.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
```