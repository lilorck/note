# Django Rest Framework的安装及初始化设置

## 安装Django-rest-framework

安装Django-rest-framework之前需要安装Django,Django和Django-rest-framework都是通过pip进行安装。  <br>
这里在虚拟环境中安装，没有在全局变量中安装。

```dos
Microsoft Windows [版本 10.0.17134.345]
(c) 2018 Microsoft Corporation。保留所有权利。

C:\Users\MisSa>f:

F:\>cd venv

F:\venv>cd Scripts

F:\venv\Scripts>activate

(venv) F:\venv\Scripts>pip install djangorestframework
Collecting djangorestframework
  Downloading https://files.pythonhosted.org/packages/99/0b/d37a5a96c5d301e23adcabcc2f3fa659fb34e6308590f95ebb50cdbe98a1/djangorestframework-3.9.0-py2.py3-none-any.whl (924kB)
    100% |████████████████████████████████| 931kB 10kB/s
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.9.0

(venv) F:\venv\Scripts>

```

## 新建空项目和app

安装之后，新建一个空项目进行练习

### 在虚拟环境中使用创建项目和app

```dos
(venv) F:\venv\Scripts>cd \

(venv) F:\>cd Django/

(venv) F:\Django>cd Django-rest-framework

// 在该路径下创建空项目afu
(venv) F:\Django\Django-rest-framework>django-admin startproject afu

(venv) F:\Django\Django-rest-framework>cd afu

(venv) F:\Django\Django-rest-framework\afu>dir
 驱动器 F 中的卷是 Project
 卷的序列号是 2A4B-2CC7

 F:\Django\Django-rest-framework\afu 的目录

2018/10/31  09:01    <DIR>          .
2018/10/31  09:01    <DIR>          ..
2018/10/31  09:01    <DIR>          afu
2018/10/31  09:01               823 manage.py
               1 个文件            823 字节
               3 个目录 53,497,532,416 可用字节

// 在该路径下创建一个app
(venv) F:\Django\Django-rest-framework\afu>python manage.py startapp musics

(venv) F:\Django\Django-rest-framework\afu>dir
 驱动器 F 中的卷是 Project
 卷的序列号是 2A4B-2CC7

 F:\Django\Django-rest-framework\afu 的目录

2018/10/31  09:02    <DIR>          .
2018/10/31  09:02    <DIR>          ..
2018/10/31  09:02    <DIR>          afu
2018/10/31  09:01               823 manage.py
2018/10/31  09:02    <DIR>          musics
               1 个文件            823 字节
               4 个目录 53,497,524,224 可用字节

(venv) F:\Django\Django-rest-framework\afu>cd musics

(venv) F:\Django\Django-rest-framework\afu\musics>dir
 驱动器 F 中的卷是 Project
 卷的序列号是 2A4B-2CC7

 F:\Django\Django-rest-framework\afu\musics 的目录

2018/10/31  09:02    <DIR>          .
2018/10/31  09:02    <DIR>          ..
2018/10/31  09:02                66 admin.py
2018/10/31  09:02                92 apps.py
2018/10/31  09:02    <DIR>          migrations
2018/10/31  09:02                60 models.py
2018/10/31  09:02                63 tests.py
2018/10/31  09:02                66 views.py
2018/10/31  09:02                 0 __init__.py
               6 个文件            347 字节
               3 个目录 53,497,524,224 可用字节
```

## 注册app

在settings.py中的INSTALLED_APPS中注册app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'musics',
]
```

## 在git库中添加新的仓库

```dos
MisSa@DESKTOP-PIQ06QO MINGW64 /
$ cd f:

MisSa@DESKTOP-PIQ06QO MINGW64 /f
$ cd Django/

MisSa@DESKTOP-PIQ06QO MINGW64 /f/Django
$ cd Django-rest-framework/

// 创建新创库 
MisSa@DESKTOP-PIQ06QO MINGW64 /f/Django/Django-rest-framework
$ git init
Initialized empty Git repository in F:/Django/Django-rest-framework/.git/

// 添加到仓库
MisSa@DESKTOP-PIQ06QO MINGW64 /f/Django/Django-rest-framework (master)
$ git  add afu/*

// 提交到仓库，备注信息：'创建了一个Django空项目，创建了一个app，里面的配置还有没进行修改。'
MisSa@DESKTOP-PIQ06QO MINGW64 /f/Django/Django-rest-framework (master)
$ git commit -m '创建了一个Django空项目，创建了一个app，里面的配置还有没进行修改。'
[master (root-commit) 5ba2490] 创建了一个Django空项目，创建了一个app，里面的配置还有没进行修改。
 14 files changed, 196 insertions(+)
 create mode 100644 afu/afu/__init__.py
 create mode 100644 afu/afu/__pycache__/__init__.cpython-36.pyc
 create mode 100644 afu/afu/__pycache__/settings.cpython-36.pyc
 create mode 100644 afu/afu/settings.py
 create mode 100644 afu/afu/urls.py
 create mode 100644 afu/afu/wsgi.py
 create mode 100644 afu/manage.py
 create mode 100644 afu/musics/__init__.py
 create mode 100644 afu/musics/admin.py
 create mode 100644 afu/musics/apps.py
 create mode 100644 afu/musics/migrations/__init__.py
 create mode 100644 afu/musics/models.py
 create mode 100644 afu/musics/tests.py
 create mode 100644 afu/musics/views.py

```

## 在新建项目中配置Django-rest-framework

## Models

定义一个数据库的表结构，并且在数据库中建立表。

## 定义model

```python
from django.db import models


# Create your models here.
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField()
    created = models.DateTimeField()

    class Mete:
        da_table = 'music'

```

## 写入数据库

```dos
(venv) F:\Django\Django-rest-framework\afu>python manage.py makemigrations
Migrations for 'musics':
  musics\migrations\0001_initial.py
    - Create model Music

(venv) F:\Django\Django-rest-framework\afu>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, musics, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying musics.0001_initial... OK
  Applying sessions.0001_initial... OK

```