from django.db.models import *


# Create your models here.
## 产品分类表
class GoodsCategory(Model):
    """产品分类"""

    name = CharField(max_length=64, verbose_name='分类名称')
    remark = CharField(max_length=64, null=True, verbose_name='备注', blank=True)


## 产品表
class Goods(Model):
    """产品"""

    # 外键
    category = ForeignKey(GoodsCategory, on_delete=SET_NULL, related_name='goods_set', null=True, verbose_name='产品分类',
                          blank=True, )
    # on_delete 

    number = CharField(max_length=32, verbose_name='产品编号')
    name = CharField(max_length=64, verbose_name='产品名称')
    barcode = CharField(max_length=32, null=True, blank=True, verbose_name='条码')
    spec = CharField(max_length=64, null=True, blank=True, verbose_name='规格')
    shelf_life_days = IntegerField(null=True, verbose_name='保质期天数')
    purchase_price = FloatField(default=0, verbose_name='采购价')
    retail_price = FloatField(default=0, verbose_name='零售价')
    remark = CharField(max_length=128, null=True, blank=True, verbose_name='备注')


"""
CharField：用于存储字符串类型，有最大长度限制
IntegerField：用于存储整数类型
FloatField：用于存储浮点数类型
BooleanField：用于存储布尔类型
DateField：用于存储日期类型
DateTimeField：用于存储日期和时间类型
ImageField：用于存储图片类型
FileField：用于存储文件类型
ForeignKey：外键 用于表示数据库表之间的关联关系
OneToOneField：一对一 用于表示一对一的关联关系
ManyToManyField：多对多 用于表示多对多的关联关系


max_length：字段的最大长度限制，可以应用于多种不同的字段类型。
verbose_name：字段的友好名称，便于在管理员后台可视化操作时使用。
default：指定字段的默认值。
null：指定字段是否可以为空。null=True 设置允许该字段为 NULL 值
blank：指定在表单中输入时是否可以为空白。
choices：用于指定字段的可选值枚举列表。
related_name：指定在多对多等关系中反向使用的名称。
on_delete：指定如果外键关联的对象被删除时应该采取什么操作。
"""
