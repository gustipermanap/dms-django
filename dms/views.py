
# from django.http import HttpResponse
# def login(request):
#     return HttpResponse('Halaman Login')
# def index(request):
#     return HttpResponse('Halaman Index')
from django.shortcuts import render
def login(request):
    return render(request,'login/login.html')
def main(request):
    return render(request,'main.html')