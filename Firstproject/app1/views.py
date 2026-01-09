from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def view1(request):
    print(request.method)
    return HttpResponse("hello world,iam from view1")
def view2(request):
    return HttpResponse("hello world, iam from view2")    
def view3(request):
    return HttpResponse("hello world, iam from view3")
def view4(request):
    return JsonResponse({"name":"Rupa","msg":"i'm from view4"})
def view5(request):
    return JsonResponse({"status":"Success","Response":"Welcome"})
def dynamicview(request):
    qp1=request.GET.get("name" , 'world') #getting query param from url
    return HttpResponse(f'hello {qp1}')
def personInfo(request):
    name=request.GET.get("name" , "rupa")
    city=request.GET.get("city" , "hyd")
    role=request.GET.get("role" , "software")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":"Info"})
def temp1(request):
    return render(request,"./simple.html")
def temp2(request):
    return render(request,"./second.html")

#json always allow object only