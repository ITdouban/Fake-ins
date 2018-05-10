# Generated by Django 2.0.2 on 2018-05-08 14:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='邮箱')),
                ('profile_picture', models.ImageField(default='/media/profile_picture/default.jpg', upload_to='media/profile_picture/', verbose_name='头像')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='用户名')),
                ('nickname', models.CharField(default='无名用户', max_length=15, verbose_name='昵称')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=2, verbose_name='性别')),
                ('address', models.CharField(max_length=40, null=True, verbose_name='地址')),
                ('introduction', models.CharField(max_length=100, null=True, verbose_name='个人简介')),
                ('birthday', models.DateField(default='2000-01-01', verbose_name='生日')),
                ('followed_num', models.IntegerField(default=0, verbose_name='被关注人数')),
                ('following_num', models.IntegerField(default=0, verbose_name='关注人数')),
                ('Reg_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('user_type', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
    ]
