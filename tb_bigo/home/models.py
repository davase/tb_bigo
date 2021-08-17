from django.db import models

#####获取对话链接
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.

#创建淘宝商家授权表
class TbserverUserToken(models.Model):
    tbid = models.CharField(max_length=500, verbose_name="淘宝id")
    tbnick = models.CharField(max_length=500, verbose_name="淘宝昵称")
    resinfo = models.CharField(max_length=2000, verbose_name="授权结果集")
    token = models.CharField(max_length=1000, verbose_name="授权码")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updatetime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    def __str__(self):
        return self.tbnick

    class Meta:
        verbose_name = verbose_name_plural = '淘宝商家授权表'
        db_table = 'tbserver_user_token'

