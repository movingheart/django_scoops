from django.shortcuts import render
import time,datetime

def current_date(request):
    current_date = time.strftime("%Y-%m-%d %X",time.localtime())  
    return render(request,'scoops/current_date.html',{'current_date':current_date})

def hours_ahead(request):
    date_delta = datetime.datetime.now()+datetime.timedelta(hours=24)
    delta = datetime.datetime.strftime(date_delta,"%Y-%m-%d %X")
    context = {'hour_offset':24,'next_time':delta}
    return render(request,'scoops/hours_ahead.html',context)
