---
title: P06 Django-admin 引入admin后台和管理员
date: 2023-06-25T15:39:15Z
lastmod: 2023-06-27T17:23:33Z
---

# P06 Django-admin 引入admin后台和管理员

## Admin

1. 创建后台 admin 管理员

    ​`python manage.py createsuperuser`​（创建超级管理员）
2. 登录 admin 后台

    ​`http://127.0.0.1:8000/admin`​

　　‍

## 配置

　　在admin.py文件中注册您的模型：

```python
from django.contrib import admin
from .models import * # 引入产品表

# 一定要分开逐个注册，不能放在一起
admin.site.register(Goods) # 在admin站点中 注册产品表
admin.site.register(GoodsCategory) # 在admin站点中 注册产品表
```

　　‍
