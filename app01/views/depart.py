from django.shortcuts import render, redirect

from app01 import models


def depart_list(request):
    depart_list = models.DepartMent.objects.all()
    return render(request, 'depart_list.html', {'depart_list': depart_list})

def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    title = request.POST.get('title')
    models.DepartMent.objects.create(title=title)
    return redirect('/depart/list/')

def depart_del(request):
    id = request.GET.get('id')
    models.DepartMent.objects.filter(id=id).delete()
    return redirect('/depart/list/')

def depart_edit(request, id):
    print('adsf')
    if request.method == "GET":
        title = models.DepartMent.objects.filter(id=id).first().title
        return render(request, 'depart_edit.html', {"title": title})
    title = request.POST.get('title')
    models.DepartMent.objects.filter(id=id).update(title=title)
    return redirect('/depart/list/')