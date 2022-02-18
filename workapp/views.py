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
    return render(request, 'exercise2.html', context)


def exercise3(request):
    context = None
    if request.method == 'POST':
        writer = request.POST.get("writer"," ")
        memo = request.POST.get("memo"," ")
        context = {
            'info':{
                'info1' : writer,
                'info2' : memo,
                }
            }
    return render(request, 'exercise3.html', context)

def product1(request):
    herfs1 = []
    images1 = []
    herfs2 = []
    images2 = []
    for i in range(5):
        herfs1 = "/workapp/basket1/?pid="+str(i)
        images1 = "/static/images/"+str(i)+".jpg"
    for i in range(5,11):
        herfs2 = "/workapp/basket1/?pid="+str(i)
        images2 = "/static/images/"+str(i)+".jpg"
    context = {
        'herfs1' : herfs1,
        'herfs2': herfs2,
        'images1' : images1,
        'images2' : images2,
    }
    return render(request, 'product1.html', context)

def basket1(request):
    dt = datetime.datetime.now()
    i = request.GET.get("pid")
    goods = "/static/images/"+i+".jpg"
    context = {
        'current_date' : dt,
        'goods' : goods
    }
    return render(request, 'basket1.html', context)