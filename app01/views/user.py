from django.shortcuts import render, redirect

from app01 import models
from app01.utils.form import UserModelForm


def user_list(request):
    user_list = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'user_list': user_list})

def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.DepartMent.objects.all()
        }
        return render(request, 'user_add.html', context)
    username = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    time = request.POST.get('time')
    gender = request.POST.get('gender')
    depart = request.POST.get('depart')
    models.UserInfo.objects.create(name=username, password=password, age=age, account=account, create_time=time,
                                   gender=gender, depart_id=depart)
    return redirect('/user/list/')

def user_model_form_add(request):
    if request.method == "GET":
        form = UserModelForm
        return render(request, 'user_model_form_add.html', {'form': form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    else:
        return render(request, 'user_model_form_add.html', {'form': form})

def user_edit(request, id):
    row_object = models.UserInfo.objects.filter(id=id).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    else:
        return render(request, 'user_edit.html', {'form': form})

def user_del(request, id):
    models.UserInfo.objects.filter(id=id).delete()
    return redirect('/user/list/')