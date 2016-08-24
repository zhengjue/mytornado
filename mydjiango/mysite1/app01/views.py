from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.


def Index(request):
    return render_to_response("index.html")
