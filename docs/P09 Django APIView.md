---
title: P09 Django APIView
date: 2023-06-26T14:54:44Z
lastmod: 2023-06-27T21:54:03Z
---

# P09 Django APIView

## Teaching Order

1. APIView 的概念

   APIview 是 Django REST Framework 提供的一个视图类。它和 Django 中的 view 类有些相似，但是又有一些不同之处。APIview 可以处理基于 HTTP 协议的请求，并返回基于内容协商的响应，它旨在提供一个易于使用且灵活的方式来构建 API 视图。
2. 如何使用

    **view.py**

   ```python
   # 面向对象编程
   from django.shortcuts import render
   from rest_framework.decorators import api_view
   from .models import *
   from rest_framework.response import Response
   from rest_framework.views import APIView
    # 面向对象编程
    class FilterGoodsCategoryAPI(APIView):
        # request 表示当前的请求对象
        # self 表示当前实例对象

        def get(self, request, format=None):
            print(request.method)
            return Response('ok')

        def post(self, request, format=None):
            print(request.method)
            return Response('ok')

        def put(self, request, format=None):
            print(request.method)
            return Response('ok')
   ```

   **url.py**

   ```python
   from apps.erp_test.views import *

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('filtergoodscategoryapi/', FilterGoodsCategoryAPI.as_view()),
   ]
   ```

   首先，self 表示当前实例对象，这里指的是视图类的实例对象。

   request 表示当前的请求对象，包含了客户端发送的信息，例如请求头、请求体等。

   pk 是 path 参数 [int:pk](int:pk)，用于获取请求中的产品 ID。

   format 表示客户端请求的响应格式，例如 JSON、XML 等。这个参数通常不需要指定，会根据客户端发送的 Accept 请求头来自动选择响应格式。如果客户端指定了响应格式，那么我们可以从请求中获取到这个参数并且做出相应的处理。

   在这个方法中，我们需要通过 pk 参数获取到对应的产品数据，并将其序列化成 JSON 格式并返回给客户端。具体的实现方式可以参考序列化器文档和 Django ORM 文档。

　　‍
