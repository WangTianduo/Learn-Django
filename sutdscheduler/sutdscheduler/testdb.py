# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# 数据库操作
def testdb(request):
    Test.objects.all().delete()
    return HttpResponse("<p>" + 'del alr' + "</p>")