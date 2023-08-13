"""
URL configuration for erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from apps.erp_test.views import *
from django.urls import include
from rest_framework import routers

# 创建DefaultRouter对象，用于生成路由
router = routers.DefaultRouter()
# 将视图集注册到路由器上，字符串里的是URL路径的前缀
router.register('GoodsCategory', GoodsCategoryViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('filtergoodscategory/', FilterGoodsCategory),
    path('insertgoodscategory/', InsertGoodsCategory),
    path('filtergoodscategoryapi/', FilterGoodsCategoryAPI.as_view()),
    path('getgoods/', GetGoods.as_view()),
]
# 把生成的url 添加到项目的url配置中
urlpatterns += router.urls
# DefaultRouter
""""
drf 提供的一个路由器
自动生成 URL 路由
和视图函数或视图集来关联使用的
"""
