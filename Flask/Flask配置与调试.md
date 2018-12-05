# Flask的配置与调试

Flask中的配置是继承自python中的dict类，因此具有所有的dict方法。同时本身也是一个字典。其中：</br>

- **`config`是Config类的实例化对象**

## 配置管理

flask中的配置方式有以下几种：

1. `obj.config['KEY'] = values`
2. `obj.config.from_pyfile('target.py')`
3. `obj.config.from_object()`
4. `obj.config.from_envvar(env)`
5. `obj.config.from_json`
6. `obj.config.from_mapping`
7. `obj.config.get_namespace`

### obj.config['KEY'] = values

简单粗暴，直接在application.py文件中使用。缺点是配置多的话太乱，不便于维护。

```python
from flask import Flask, current_app

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def root_():
    conf = current_app.config
    print(conf)
    return 'Conf'


if __name__ == '__main__':
    app.run()
```

### 从py文件中导入

从编辑好的py文件中导入，在py文件中直接编辑配置，配置名大写。

application.py中：

```python
from flask import Flask, current_app

app = Flask(__name__)
app.config.from_pyfile('path/to/config.py', silent=True)

@app.route('/')
def root_():
    conf = current_app.config
    print(conf) 
    return 'Conf'


if __name__ == '__main__':
    app.run()
```

config.py中：

```python
DEBUG = True
```

### 从自定义环境导入

- `obj.config.from_envvar(env)`
- **内部调用的是`from_pyfile`方法**

导入编辑好的配置，生成一个环境配置。

application.py中：

```python
from flask import Flask, current_app
import os


os.environ['FLASK_SETTINGS'] = 'FlaskConfig.py'

app = Flask(__name__)
app.config.from_envvar('FLASK_SETTINGS')

@app.route('/')
def root_():
    conf = current_app.config
    print(conf)
    return 'Conf'


if __name__ == '__main__':
    app.run()
```

config.py

```python
DEBUG = True
NAME = 'Roc'
AGE = 18
```

### 从对象导入

- app.config.from_object()

此方法是需要把配置文件的相关配置写成类属性，来实现调用。

application.py中：

```python
from flask import Flask, current_app

app = Flask(__name__)
app.config.from_object('FlaskConfig.Info')


@app.route('/')
def root_():
    conf = current_app.config
    print(conf)
    return 'Conf'


if __name__ == '__main__':
    app.run()
```

config.py:

```python
class BaseConf(object):
    DEBUG = True

class Info(BaseConf):
    NAME = 'Roc'
    AGE = 18
```

### 从Json文件中导入

从Json文件格式导入，内部执行的是`json.loads()`方法

```python
from flask import Flask, current_app

app = Flask(__name__)
app.config.from_json('config.json')


@app.route('/')
def root_():
    conf = current_app.config
    print(conf)
    return 'Conf'


if __name__ == '__main__':
    app.run()
```

config.json:

```json
{
    "DEBUG": true,
    "NAME": "Roc",
    "AGE": 18
}
```

### from_mapping

该方法中传入的是字典。

```python
from flask import Flask, current_app

app = Flask(__name__)
app.config.from_mapping({"DEBUG": True, "NAME": "RocS"})


@app.route('/')
def root_():
    conf = current_app.config
    print(conf)
    return 'Conf'


if __name__ == '__main__':
    app.run()
```

### get_namespace

此方法待补充
