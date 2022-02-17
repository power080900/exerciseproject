from django.shortcuts import render

import datetime

# Create your views here.
def exercise1(request):
    today = datetime.date.today()
    m = today.month
    d = today.day
    context = {'month':m, 'date':d}
    return render(request,'exercise1.html',context)

def exercise2(request):
    query = 'type' in request.GET
    if query :
        a = request.GET['type']
        if a == 'number':
            type = '우리팀 인원은 4명입니다'
            image = '/static/images/olaf2.png'
            context = {
                'type': type,
                'image': image,}
        elif a == 'memberlist':
            type = '우리팀의 팀원을 소개합니다'
            image = '/static/images/olaf1.png'
            context = {
                'type': type,
                'image': image,
                'members':['박성민','박환','오병권','이경재']}
    else :
        type = 'type=memberlist 또는 type=number로 쿼리를 전달하세요'
        image = '/static/images/olaf1.png'
        context = {
            'type': type,
            'image': image,
    }
    return render(request, 'exercise2.html',context)