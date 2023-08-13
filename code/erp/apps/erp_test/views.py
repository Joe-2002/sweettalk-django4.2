from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializer import *
from rest_framework.decorators import action

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet


#### modelviewset
class GoodsCategoryViewSet(ModelViewSet):
    # 指定查询集（用到的数据）
    queryset = GoodsCategory.objects.all()
    # 指定查询集用到的序列化容器
    serializer_class = GoodsCategorySerilizer

    @action(detail=False, methods=['get'])
    def latest(self, request):
        latest_obj = GoodsCategory.objects.latest('id')
        print(latest_obj)
        return Response("helllo 你调用了自定义的函数")
    
    @action(detail=False, methods=['get','post'])
    def delete_example(self, request):
        name = request.data.get('name')
        # 删除名称为 'name' 的商品
        categories_to_delete = GoodsCategory.objects.filter(name=name)
        # 使用delete()方法删除对象
        deleted_count= categories_to_delete.delete()
        print(f"Deleted {deleted_count} categories.")    
    
    @action(detail=False, methods=['get','post'])
    def create_example(self, request):
        name = request.data.get('name')
            # 使用create()方法创建新的商品分类对象
        created_category = GoodsCategory.objects.create(name)
        print("Created category:", created_category)     
# Create your views here.
# GET
# POST

#### 函数式编程
@api_view(['POST', 'GET'])
def FilterGoodsCategory(request):
    if request.method == 'GET':
        print(request.method)
    if request.method == 'POST':
        print(request.method)
    data = request.data.get('分类名字')
    goods_category = get_object_or_404(GoodsCategory, name=data)
    print(goods_category)
    # ans = Goods.objects.filter(category=goods_category).all().values()
    # print(ans)
    goods = Goods.objects.filter(category=goods_category)
    serializer = GoodsSerializer(goods, many=True)  # 请确保导入合适的序列化器

    # 输出对象 和 数据类型
    print("object type:", type(Goods.objects))
    print("object.all() type:", type(Goods.objects.all()))
    print("object.all().values type:", type(Goods.objects.all().values()))

    # Instance
    print("object.get(id=1) type:", type(Goods.objects.get(id=1)))

    return Response(serializer.data)
    # return Response(ans)

@api_view(['POST', 'GET'])
def InsertGoodsCategory(request):
    category_name = request.data.get('分类名字')
    
    # 获取分类对象或创建新的分类对象
    category, created = GoodsCategory.objects.get_or_create(name=category_name)
    
    # 判断是否已存在分类
    if not created:
        return Response({"status": "已存在", "goods_category": category_name}, status=200)
    else:
        return Response({"message": f"Successfully inserted category '{category_name}'."})


@api_view(['POST','GET'])
def FilterGoodsCategory(request):
    data = request.data.get('分类名字')
    goods = GoodsCategory.objects.filter(name=data)
    if goods.exists():
        return Response({"status": "已存在", "goods_category": data}, status=200)
    else:
        return Response({"status": "不存在" ,"goods_category": data}, status=404)

#### APIView
class GetGoods(APIView):
    def get(self, request):
        data = Goods.objects.all()
        serializer = GoodsSerializer(instance=data, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        # 从请求数据中提取字段
        request_data = {
            "category": request.data.get("Goodscategory"),
            "number": request.data.get("number"),
            "name": request.data.get("name"),
            "barcode": request.data.get("barcode"),
            "spec": request.data.get("spec"),
            "shelf_life_days": request.data.get("shelf_life_days"),
            "purchase_price": request.data.get("purchase_price"),
            "retail_price": request.data.get("retail_price"),
            "remark": request.data.get("remark"),
        }

        # 使用 create() 方法创建新的商品对象
        new_goods = Goods.objects.create(**request_data)

        # 对创建的对象进行序列化，并作为响应返回
        serializer = GoodsSerializer(instance=new_goods)
        return Response(serializer.data)

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



""""
1. 先获取分类的名字
2. 根据分类的名字，在分类表中，获取键
3. 根据键，筛选出分类下的数据
"""


# QuerySet
""""
objects返回的 查询集合
类似一个列表，包含很多数据
包含了若干个Instance
常用的操作：筛选（filter）、删除、更新等
"""


# Instance
"""
单个实力
类似数据库中的一行数据
主要对单个对象（实例）做操作
常用操作：创建、更新、删除等
"""


"""
ModelViewSet 是我们顶层的一个 模型类
Restful API
根据动作来的
get、post、put、delete


APIView 是我们底层的一个

ModelViewSet的组成：
GenericViewSet、提供通用的视图方法
ListModelMixin、提供 list 获取一个列表 get
RetrieveModelMixin、 提供 retrieve 获取单个数据（详细信息） get 后跟pk 指定的一个数据的id
CreateModelMixin、 提供 create 创建数据 post
UpdateModelMixin、 提供 update 更新数据 put 后跟pk 指定的一个数据的id
DestoryModelMixin 提供 destroy 删除数据 delete 后跟pk 指定的一个数据的id
自定义 


默认的增删查改的功能
"""
