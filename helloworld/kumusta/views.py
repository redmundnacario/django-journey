from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def viewKumustaPage(request):
    return HttpResponse('Kumusta means Hello in Filipino.')