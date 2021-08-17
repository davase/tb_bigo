# Generated by Django 3.0 on 2021-08-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbserverUserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tbid', models.CharField(max_length=500, verbose_name='淘宝id')),
                ('tbnick', models.CharField(max_length=500, verbose_name='淘宝昵称')),
                ('resinfo', models.CharField(max_length=2000, verbose_name='授权结果集')),
                ('token', models.CharField(max_length=1000, verbose_name='授权码')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '淘宝商家授权表',
                'verbose_name_plural': '淘宝商家授权表',
                'db_table': 'tbserver_user_token',
            },
        ),
    ]
