# _*_ coding:utf-8  _*_
from django.shortcuts import render, render_to_response, redirect

# Create your views here.

def index(request):
    return render_to_response("index.html")

