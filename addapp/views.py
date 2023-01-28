from django.shortcuts import render
from django.http import HttpResponse
def welcome (request):
    res=HttpResponse("""<html><body bgcolor=cyan><center><h1>welcome to lokesh it</h1></center></body></html>""")
    return res