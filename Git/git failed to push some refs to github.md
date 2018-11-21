# Git推送到GitHub仓库失败

使用Git将文件推送至GitHub的远程仓库时，报错`failed to push some refs to 'git@github.com:RocsSun/mytest.git'`

```shell

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git remote add origin git@github.com:RocsSun/mytest.gt

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git push -u origin master
Warning: Permanently added the RSA host key for IP address '52.74.223.119' to the list of known hosts.
ERROR: Repository not found.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git remote add origin git@github.com:RocsSun/mytest.git
fatal: remote origin already exists.

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git remote rm origin

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git remote add origin git@github.com:RocsSun/mytest.git

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git push -u origin master
To github.com:RocsSun/mytest.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:RocsSun/mytest.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git push  origin master
To github.com:RocsSun/mytest.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:RocsSun/mytest.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Roc@DESKTOP-AF552U2 MINGW64 /e/note (master)
$ git remote rm origin

```

大概原因就是 意思是本地和远程的文件应该合并后才能上传本地的新文件

1、先拉下来，会自动合并的（不用操心）

git pull origin master

2、再上传

git push -u origin master

成功解决问题