from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.http import urlencode

from config.settings import UPLOAD_DIR
from frame.cartdb import CartDB
from frame.custdb import CustDB
from frame.error import ErrorCode
from frame.itemdb import ItemDB


def home(request):
    return render(request, 'home.html');

def login(request):
    return render(request, 'login.html')

def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    next = 'home.html';
    try:
        cust = CustDB().selectone(id);
        if pwd == cust.pwd:
            request.session['logincust'] =  {'id':cust.id,'name':cust.name};
            context = None;
        else:
          raise Exception;
    except:
        context = { 'msg':ErrorCode.e0003 };
        next = 'error.html';
    return render(request, next, context);

def logout(request):
    if request.session['logincust'] != None:
        del request.session['logincust'];
    return render(request,'home.html');

def inputcart(request):
    custid = request.GET['custid'];
    itemid = request.GET['itemid'];
    num = request.GET['num'];
    CartDB().insert(custid, int(itemid), int(num));
    return redirect('itemlist');

def cartlist(request):
    custid = request.GET['custid'];
    cartlist = CartDB().select(custid);
    context = {'cartlist':cartlist};
    return render(request, 'cartlist.html', context);


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
    # print(id, pwd, name)
    try:
        CustDB().insert(id, pwd, name);
    except:
        context = {'msg': ErrorCode.e0001}
        return render(request, 'error.html',context);
    # 조회 화면으로 이동한다.
    return redirect('custlist');

def custupdate(request):
    id = request.GET['id'];
    cust = CustDB().selectone(id);
    context = {'c': cust};  # clist를 cl이라는 변수에 넣음
    return render(request, 'custupdate.html', context);

def custupdateimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    CustDB().update(id, pwd, name);
    # custdetail?id=01&name=?? 을 만들기 위해서//쿼리스트링을 붙이기 위해...
    qstr = urlencode({'id': id});
    return HttpResponseRedirect('%s?%s' % ('custdetail', qstr));

def itemlist(request):
    items = ItemDB().select();
    context = {
        'ilist':items
    }
    return render(request, 'itemlist.html', context);


def itemadd(request):
    return render(request, 'itemadd.html');
def itemaddimpl(request):
    name = request.POST['name'];
    price = request.POST['price'];
    imgname = '';
    if 'img' in request.FILES:
        img = request.FILES['img'];
        imgname = img._name;
        fp = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
        for chunk in img.chunks():
            fp.write(chunk);
            fp.close();
    ItemDB().insert(name, int(price), imgname);
    return redirect('itemlist')

def itemdetail(request):
    id = request.GET['id'];
    item = ItemDB().selectone(int(id));
    context = { 'i': item }
    return render(request, 'itemdetail.html', context);

def itemdelete(request):
    id = request.GET['id'];
    item = ItemDB().delete(int(id));
    context = { 'i': item }
    return rendirect('itemlist');

def itemupdate(request):
    id = request.GET['id'];
    item = ItemDB().selectone(int(id));
    context = { 'i': item }
    return render(request, 'itemupdate.html', context);

def itemupdateimpl(request):
    id = request.POST['id'];
    name = request.POST['name'];
    price = request.POST['price'];
    oldimgname = request.POST['oldimgname'];
    imgname = '';
    if 'newimg' in request.FILES:
        newimg = request.FILES['newimg'];
        imgname = newimg._name;
        fp = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
        for chunk in newimg.chunks():
            fp.write(chunk);
            fp.close();
    else:
        imgname = oldimgname;

    ItemDB().update(int(id), name, int(price), imgname)
    qstr = urlencode({'id': id});
    return HttpResponseRedirect('%s?%s' % ('itemdetail', qstr));








