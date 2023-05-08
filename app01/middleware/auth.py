from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 排除不需要登入就能訪問的頁面
        # request.path_info 獲取當前請求的URL
        if request.path_info in ["/login/", "/image/code/"]:
            return
        # 讀取當前用戶的session
        info_dict = request.session.get('info')
        if info_dict:
            return
        return redirect('/login/')