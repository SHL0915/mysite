from django.shortcuts import render
from django.http import HttpResponse
from urllib3 import HTTPResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    # view.index 내부에서는 리스폰스를 발생시킴.