from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.models import User


@csrf_exempt
def user(request):
    if request.method == "GET":
        username = request.GET.get("username")
        print(username)
        print("GET 查询")
        return HttpResponse("GET OK")
    if request.method == "POST":
        print("POST 新增")
        return HttpResponse("POST OK")
    if request.method == "PUT":
        print("PUT 修改")
        return HttpResponse("PUT OK")
    if request.method == "DELETE":
        print("DELETE 删除")
        return HttpResponse("DELETE OK")

@method_decorator(csrf_exempt, name="dispatch")
class Users(View):
    def get(self,request,*args,**kwargs):
        user_id=kwargs.get("id")
        if user_id:
            user_val = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            print(user_val)
            if user:
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户",
                    "results": user_val
                })
        else:
            user_all = User.objects.all().values("username", "password", "gender")
            if user_all:
                return JsonResponse({
                    "status": 200,
                    "message:": "查询所有用户",
                    "results": list(user_all)
                })

            return JsonResponse({
                "status": 400,
                "message": "查询用户失败",
            })
    def post(self,request,*args,**kwargs):
        username=request.POST.get("username")
        password=request.POST.get("password")
        gender=request.POST.get("gender")
        print(username)
        print(password)
        print(gender)

        try:
            user=User.objects.create(username=username,password=password,gender=gender)
            return JsonResponse({
                "status": 200,
                "message": "新增单个用户",
                "results": {"username": username, "password":password,"gender": user.gender}
            })
        except:
            return JsonResponse({
                "status": 400,
                "message": "新增失败",
            })
    def delete(self,request,*args,**kwargs):
        delete_id=kwargs.get("id")
        delete_user=User.objects.filter(pk=delete_id).values()
        try:
            if delete_user:
                print(234)
                User.objects.get(id=delete_id).delete()
                print(345)
                return JsonResponse({
                    "status":200,
                    "message":"删除成功"
                })
            return JsonResponse({
                "status":200,
                "message":"删除失败,该用户已经不存在",

            })
        except:
            print(123)
            return JsonResponse({
                "status":400,
                "message":"删除失败",
            })