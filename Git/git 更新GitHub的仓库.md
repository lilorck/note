# 更新GitHub的仓库

在GitHub上仓库已经存在且提交过，本地仓库部分更新后推送至GitHub仓库

## 添加，提交至本地仓库

将改动文件添加并提交到仓库

```dos
Roc@DESKTOP-AF552U2 MINGW64 /e/note/Git (master)
$ git add 'git 报错 index file corrupt.md'

Roc@DESKTOP-AF552U2 MINGW64 /e/note/Git (master)
$ git commit -m '新增git提交到仓库报错分析'
[master 0b068c4] 新增git提交到仓库报错分析
 1 file changed, 60 insertions(+)
 create mode 100644 "Git/git \346\212\245\351\224\231 index file corrupt.md"
```

## 拉取远程仓库

拉取当前分支最新代码:

- git pull

```dos
Roc@DESKTOP-AF552U2 MINGW64 /e/note/Git (master)
$ git pull
Already up to date.
```

## 推送到GitHub仓库

push到远程master分支上：

- git push origin master

```dos
Roc@DESKTOP-AF552U2 MINGW64 /e/note/Git (master)
$ git push origin master
Warning: Permanently added the RSA host key for IP address '13.250.177.223' to the list of known hosts.
Enumerating objects: 31, done.
Counting objects: 100% (31/31), done.
Delta compression using up to 4 threads
Compressing objects: 100% (25/25), done.
Writing objects: 100% (25/25), 6.66 KiB | 1.11 MiB/s, done.
Total 25 (delta 14), reused 0 (delta 0)
remote: Resolving deltas: 100% (14/14), completed with 4 local objects.
To github.com:RocsSun/note.git
   53ab25a..d9ccf3e  master -> master
```