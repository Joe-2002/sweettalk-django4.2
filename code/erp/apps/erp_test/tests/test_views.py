# -*- coding: utf-8 -*-
"""
@File : test_views.py
Description: Description of your file.
@Time : 2024/1/14 22:52
"""
from rest_framework.test import APITestCase
from rest_framework import status
from apps.erp_test.models import GoodsCategory


class GoodsCategoryViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        GoodsCategory.objects.create(name='电子产品')

    def test_get_categories(self):
        response = self.client.get('/GoodsCategory/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class GetGoodsTest(APITestCase):
    def test_get_goods(self):
        response = self.client.get('/getgoods/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
