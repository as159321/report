from io import BytesIO

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.code import check_code
from app01.utils.encrypt import md5


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用戶名",
        widget=forms.TextInput(),
        required=True
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="驗證碼",
        widget=forms.TextInput,
        required=True
    )
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get("image_code", "")
        if code.upper() != user_input_code:
            form.add_error('code', '驗證碼錯誤')
            return render(request, 'login.html', {'form': form})
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error('password', '用戶名或密碼錯誤')
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/admin/list/')
    return render(request, 'login.html', {'form': form})

def image_code(request):
    img, code_str = check_code()
    print(code_str)
    request.session['image_code'] = code_str
    # 給session設置60秒超時
    request.session.set_expiry(60)
    # 寫入內存(BytesIO)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())

def logout(request):
    request.session.clear()
    return redirect('/login/')