from django.db import models

# Create your models here.

class DepartMent(models.Model):
    """ 部門資料 """
    title = models.CharField(verbose_name='標題', max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """ 員工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密碼", max_length=64)
    age = models.IntegerField(verbose_name="年齡")
    account = models.DecimalField(verbose_name="帳戶餘額", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="創建時間")
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性別", choices=gender_choices)
    # 約束
    # on_delete=models.CASCADE() 表示如果連接鍵那個資料庫的那行被刪掉，關聯的也會被刪掉
    # null=True,blank=True, on_delete=SET_NULL 表示如果連接鍵那個資料庫的那行被刪掉，關聯的變成NULL
    depart = models.ForeignKey(verbose_name="部門", to="DepartMent", to_field="id", on_delete=models.CASCADE)


class PrettyNum(models.Model):
    """ 手機號碼表 """
    mobile = models.CharField(verbose_name="手機號", max_length=10)
    price = models.IntegerField(verbose_name="價格", default=0)
    level_choices = (
        (1, "1級"),
        (2, "2級"),
        (3, "3級"),
        (4, "4級"),
    )
    level = models.SmallIntegerField(verbose_name="級別", choices=level_choices, default=1)
    status_choices = (
        (1, "已占用"),
        (2, "未使用")
    )
    status = models.SmallIntegerField(verbose_name="狀態", choices=status_choices, default=2)

class Admin(models.Model):
    username = models.CharField(verbose_name="用戶名", max_length=32)
    password = models.CharField(verbose_name="密碼", max_length=64)

    def __str__(self):
        return self.username

class Task(models.Model):
    level_choices = (
        (1, '緊急'),
        (2, '重要'),
        (3, '臨時'),
    )
    level = models.SmallIntegerField(verbose_name="級別", choices=level_choices, default=1)
    title = models.CharField(verbose_name="標題", max_length=64)
    detail = models.TextField(verbose_name="詳細訊息")
    user = models.ForeignKey(verbose_name="負責人", to="Admin", on_delete=models.CASCADE)