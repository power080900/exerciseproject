from django.shortcuts import render

import datetime

# Create your views here.
def exercise1(request):
    today = datetime.date.today()
    m = today.month
    d = today.day
    context = {'month':m, 'date':d}
    return render(request,'exercise1.html',context)