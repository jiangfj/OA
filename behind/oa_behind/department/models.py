from django.db import models

# Create your models here.
from django.db import models

#部门表
class Department(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('部门名称',max_length=16,unique=True)

#职位表
class Position(models.Model):
    id = models.AutoField('id',primary_key=True)
    name = models.CharField('职位名称',max_length=16,default='')
    dep_name = models.CharField('部门名称',max_length=16)
    description = models.CharField('职位描述',max_length=64,default='')
    department = models.ForeignKey(Department,on_delete=models.PROTECT)

