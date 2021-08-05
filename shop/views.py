from django.shortcuts import render, redirect

# Create your views here.
from frame.custdb import CustDB
from frame.error import ErrorCode


def home(request):
    return render(request, 'home.html');

def custlist(request):
    clist = CustDB().select();
    context = {'cl':clist}; # clist를 cl이라는 변수에 넣음
    return render(request, 'custlist.html', context);

def custdetail(request):
    id = request.GET['id'];
    cust = CustDB().selectone(id);
    context = {'c': cust};  # clist를 cl이라는 변수에 넣음
    return render(request, 'custdetail.html', context);

def custdelete(request):
    id = request.GET['id'];
    CustDB().delete(id);
    return redirect('custlist');

def custadd(request):
    return render(request, 'custadd.html');

def custaddimpl(request):
    # id, pwd, name 을 입력받아 데이터베이스에 입력하고
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    print(id, pwd, name)
    try:
        CustDB().insert(id, pwd, name);
    except:
        context = {'msg': ErrorCode.e0001}
        return render(request, 'error.html',context);
    # 조회 화면으로 이동한다.
    return redirect('custlist');



def itemlist(request):
    return render(request, 'itemlist.html');
def itemadd(request):
    return render(request, 'itemadd.html');

