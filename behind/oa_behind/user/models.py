from django.db import models
import random

def default_sign():
    signs = ['健身达人','IT老兵','大馋猫','太极高手','武林败类','飞天茅台']
    return random.choice(signs)

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField('用户名',max_length=20,primary_key=True)
    nickname = models.CharField('昵称',max_length=20)
    email = models.EmailField('邮箱')
    password = models.CharField(max_length=32)
    sign = models.CharField('个人签名',max_length=50,default=default_sign)
    info = models.CharField('个人简介',max_length=50,default='')
    avatar = models.ImageField(upload_to='avatar',null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=11,default='')
    # 是否激活(默认0 未激活,1 激活)
    isActive = models.IntegerField('是否激活',default=0)
    # 是否入职（默认0 未入职，1 入职）
    is_induction = models.IntegerField('是否入职', default=0)