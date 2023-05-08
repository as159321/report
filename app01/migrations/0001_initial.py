# Generated by Django 3.2.16 on 2022-11-29 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartMent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='標題')),
            ],
        ),
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, verbose_name='手機號')),
                ('price', models.IntegerField(default=0, verbose_name='價格')),
                ('level', models.SmallIntegerField(choices=[(1, '1級'), (2, '2級'), (3, '3級'), (4, '4級')], default=1, verbose_name='級別')),
                ('status', models.SmallIntegerField(choices=[(1, '已占用'), (2, '未使用')], default=2, verbose_name='狀態')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密碼')),
                ('age', models.IntegerField(verbose_name='年齡')),
                ('accound', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='帳戶餘額')),
                ('create_time', models.DateField(verbose_name='創建時間')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性別')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department', verbose_name='部門')),
            ],
        ),
    ]