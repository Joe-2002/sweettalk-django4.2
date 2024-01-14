# 教程项目代码

使用vscode或pycharm工具打开`erp`目录，打开终端
```bash
cd erp

# 创建一个虚拟环境，erp_venv为虚拟环境名字，可自行更改
## 方式一（创建虚拟环境的python版本与本机的python版本相同）：
python -m venv erp_venv

## 方式二（推荐，可以指定python版本）：
pip install virtualenv
virtualenv erp_venv --python=python3.9

## 创建完成后erp中会生成一个名为erp_venv的虚拟环境目录


# 激活虚拟环境
## MacOS/Unix/Linux风格
source erp_venv/bin/activate

## windows风格
# TODO: windows 风格待补充

## 激活虚拟环境后，在终端的命令行前面会出现(erp_venv)


# 安装项目依赖环境
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 运行本项目代码
## 数据库迁移（由于本项目自带数据库db.sqlite3，此步骤可不执行）
### 生成迁移文件
python manage.py makemigrations
### 执行迁移
python manage.py migrate

## 运行django项目（8000为自定义端口，可自行修改）
python manage.py runserver 8000
```

