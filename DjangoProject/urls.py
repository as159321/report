"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01.views import view, depart, user, pretty, admin, account, task

urlpatterns = [
    path('', view.index),

    ######### 部門 ###########
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/del/', depart.depart_del),
    path('depart/edit/<int:id>/', depart.depart_edit),

    ######### user ###########
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/edit/<int:id>', user.user_edit),
    path('user/del/<int:id>', user.user_del),

    ########## pretty ###########
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/edit/<int:id>', pretty.pretty_edit),

    # 管理員管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/edit/<int:id>', admin.admin_edit),
    path('admin/del/<int:id>', admin.admin_del),
    path('admin/reset/<int:id>', admin.admin_reset),

    # 登入
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    # 任務管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),
]
