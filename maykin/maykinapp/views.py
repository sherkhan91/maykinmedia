from posixpath import dirname
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Hotel,City
import pathlib
import sys  


""" basic index page"""
""" html page is rendered to view the cities and hotels """
def index(request):
    if request.method == 'POST':
        print(request.POST['cities'])
        city = request.POST['cities']
        city_id = City.objects.get(city_code=city).id
        hotels = Hotel.objects.filter(city=city_id)
        cities = City.objects.all()
        context_hotels ={
            'hotels':hotels,
            'cities':cities,
        }
        return render(request,'maykinapp/index.html',context_hotels)
    
    if request.method == 'GET':
        cities = City.objects.all()

        context = {
            'cities':cities,
        }
        return render(request, 'maykinapp/index.html', context)

""" function to start corn job for first time """
"""  we can start through windows task scheduler or directly run or any other scheduler"""
def startcornjob(request):
    dir_path = pathlib.Path(__file__).resolve().parent.parent
    sys.path.append(dir_path)  
    from csv_to_model_script import main #scriptName without .py extension 
    return HttpResponse('The corn job has been started! You can close this tab now.')