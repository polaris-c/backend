# coding:utf-8
from django.db import models

class person(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    # position = models.CharField(max_length = 50)

    def composite(self):
        return self.name + ' GOOD! '

    composite.short_description = "Name and Age:"

    composite_info = property(composite)

    def __str__(self):
        return self.name

print("****** models is running ******")






