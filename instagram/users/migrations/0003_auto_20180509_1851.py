# Generated by Django 2.0.2 on 2018-05-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180509_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='-', max_length=40, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.TextField(default='-', max_length=100, null=True, verbose_name='个人简介'),
        ),
    ]