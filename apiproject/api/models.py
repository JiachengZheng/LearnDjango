# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title