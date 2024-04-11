# -*- coding: utf-8 -*-
"""
@File : test_models.py
Description: Description of your file.
@Time : 2024/1/14 22:52
"""
from django.test import TestCase
from apps.erp_test.models import Goods, GoodsCategory


class GoodsCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 设置测试数据
        GoodsCategory.objects.create(name='电子产品')

    def test_name_label(self):
        category = GoodsCategory.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, '分类名称')

    def test_name_max_length(self):
        category = GoodsCategory.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 64)


class GoodsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建分类
        category = GoodsCategory.objects.create(name='电子产品')
        # 创建商品
        Goods.objects.create(category=category, number='001', name='手机')

    def test_number_label(self):
        goods = Goods.objects.get(id=1)
        field_label = goods._meta.get_field('number').verbose_name
        self.assertEqual(field_label, '产品编号')

    def test_number_max_length(self):
        goods = Goods.objects.get(id=1)
        max_length = goods._meta.get_field('number').max_length
        self.assertEqual(max_length, 32)
