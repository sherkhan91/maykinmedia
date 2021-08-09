from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
""" basic index page"""
# def index(request):
    # return HttpResponse("Hello, Welcome to MaykinMedia hotel search app!")

""" basic index page"""
def index(request):
    template = loader.get_template('maykinapp/index.html')
    name_list = ['sher','khan','mari']
    context = {
        'name_list':name_list,
    }
    return HttpResponse(template.render(context, request))