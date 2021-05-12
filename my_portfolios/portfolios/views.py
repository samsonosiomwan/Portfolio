from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import PersonalData,Projects
# Create your views here.



def index(request):
    personal_datas = PersonalData.objects 
    projects = Projects.objects
    return render(request,'portfolios/index.html',{'personal_data':personal_datas, 'projects':projects})

def about(request):
    return render(request, 'portfolios/about.html')

def portfolio(request):
    return render(request, 'portfolios/portfolio.html')


    
