# 上传文件

Flask中上传文件的基本流程是这样的：

1. 一个`<form>`标签被标记有`enctype=multipart/form-data`，并且在里面包含一个`<input type=file>`标签。
2. 服务端应用通过请求对象上的`files`字典访问文件。
3. 使用文件的`save()`方法将文件永久地保存在文件系统上的某处。

上传文件的初步功能能

```python
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

# 设置上传目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')

# 允许上传的文件格式
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'md'])

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR


def allowed_file(filename):
    return '.' in filename and \
           filename.split('.')[1]


@app.route('/', methods=['GET', "POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
            return 'Successfully!'

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
    '''


if __name__ == '__main__':
    app.run()

```

