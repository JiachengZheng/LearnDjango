# -*- coding: utf-8 -*-
from .models import Article, Category
from rest_framework import viewsets
from .serializers import ArticleSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import fetch
import json

#根据分类查询文章列表
@csrf_exempt
def list_by_category(request):
    c_id = request.GET.get('cid', '')
    fetch.update_data(c_id)
    return fetch_list(request)

def fetch_list(request):
    c_id = request.GET.get('cid', '')
    try:
        articles = Article.objects.filter(category__pk=c_id)
    except articles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(articles, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        articles.delete()
        return HttpResponse(status=204)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
