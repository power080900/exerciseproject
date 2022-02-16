from django.shortcuts import render

import datetime

# Create your views here.



def exercise1(request):
    today = datetime.date.today()
    m = today.month
    d = today.day
    month = request.GET.get('month',m)
    date = request.GET.get('date',d)
    context = {'month':month, 'date':date}
    return render(request,'exercise1.html',context)