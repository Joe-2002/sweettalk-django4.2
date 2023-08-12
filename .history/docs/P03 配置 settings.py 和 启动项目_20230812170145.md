---
title: P03 配置 settings.py 和 启动项目
date: 2023-06-21T14:55:06Z
lastmod: 2023-06-27T17:23:24Z
---

# P03 配置 settings.py 和 启动项目

1. 设置**setting.py**文件

    加入安装的库

    ```python
    'apps.erp_test',
    'rest_framework',
    'django_filters',
    'drf_spectacular',
   
    ```

    加入新增的APP

    ```python
     'apps.erp_test'
    ```

    ​![image](assets/image-20230524160454-azcc2ka.png)​

2. 启动项目

   ```python
       运行项目先执行数据库相关操作，再启动 django 项目

    1. ​`python manage.py makemigrations`​​​​
    2. ​`python manage.py migrate`​​​​
    3. ​`python manage.py runserver`
    ```

　　‍
