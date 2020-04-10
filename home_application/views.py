# -*- coding: utf-8 -*-
import urllib3
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def hello(request):
    data = {"msg": "welcome to buleking", "data": "test data", "status": 200}
    url = 'https://paas-class.bktencent.com/api/c/compapi/v2/bk_paas/get_app_info/'
    # url = 'https://api.oioweb.cn/api/weather.php'
    params = {
        "bk_app_code": "djangodevops",
        "bk_app_secret": "371403e0-cfc6-4da5-8396-0535e14dc07e",
    }
    http = urllib3.PoolManager()
    ret = http.request('GET', url, params)
    print(type(ret), ret)
    return HttpResponse(ret.data)
    # return render(request, "home_application/hello.html")


def home(request):
    """
    首页
    """
    return render(request, 'home_application/index_home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render(request, 'home_application/dev_guide.html')


def contact(request):
    """
    联系页
    """
    return render(request, 'home_application/contact.html')
