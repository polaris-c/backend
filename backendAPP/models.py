# coding:utf-8
from django.db import models

class person(models.Model):
	name = models.CharField(max_length = 30)
	age = models.IntegerField()

	def __str__(self):
	    return self.name