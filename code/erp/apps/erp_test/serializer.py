# 序列化器


"""
序列化：把 queryset 和 instance 转换为 json/xml/yaml 等格式，返回给前端
序列化、反序列化

主要使用 ModelSerializer 来构建序列化

1. 构建序列化
2. 序列化单个字段
3. 序列化多个字段
4. 序列化所有字段

5. 序列化单个对象
6. 序列化多个对象
7. 序列关联对象（有外键）
"""

from rest_framework.serializers import *
from .models import *


class GoodsCategorySerilizer(ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'




# 构建产品序列化器
class GoodsSerializer(ModelSerializer):

    # 外键字段相关的数据 需要单独写
    category = GoodsCategorySerilizer()

    class Meta:
        # 指定需要序列化的表
        model = Goods
        # 指定我们需要序列化的字段
        fields = '__all__'