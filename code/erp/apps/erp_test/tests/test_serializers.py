# -*- coding: utf-8 -*-
"""
@File : test_serializers.py
Description: Description of your file.
@Time : 2024/1/14 22:52
"""
from django.test import TestCase

from apps.erp_test.models import GoodsCategory, Goods
from apps.erp_test.serializer import GoodsSerializer


class GoodsSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = GoodsCategory.objects.create(name='电子产品')
        Goods.objects.create(category=category, number='001', name='手机')

    def test_goods_serialization(self):
        goods = Goods.objects.get(number='001')
        serializer = GoodsSerializer(goods)
        data = serializer.data
        self.assertEqual(data['name'], '手机')
