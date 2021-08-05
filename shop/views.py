from django.shortcuts import render

# Create your views here.
from frame.custdb import CustDB


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
    return None;

def custadd(request):
    return render(request, 'custadd.html');
def itemlist(request):
    return render(request, 'itemlist.html');
def itemadd(request):
    return render(request, 'itemadd.html');

