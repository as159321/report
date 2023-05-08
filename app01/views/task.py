import json

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.bootstrap import BootStrapModelForm


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput
        }


def task_list(request):
    form = TaskModelForm()
    return render(request, 'task_list.html', {'form': form})


@csrf_exempt
def task_ajax(request):
    print(request.POST)
    data_dict = {'status': True, 'data': ['11', '22', '33', '44']}
    return HttpResponse(json.dumps(data_dict))

@csrf_exempt
def task_add(request):
    print(request.POST)
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {'status': True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {'status': False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))