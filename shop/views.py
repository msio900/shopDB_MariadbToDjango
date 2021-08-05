from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html');

def custlist(request):
    return render(request, 'custlist.html');
def custadd(request):
    return render(request, 'custadd.html');
def itemlist(request):
    return render(request, 'itemlist.html');
def itemadd(request):
    return render(request, 'itemadd.html');

