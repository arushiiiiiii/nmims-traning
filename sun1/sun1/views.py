from itertools import product
from django.http import HttpResponse
from django.shortcuts import render

def PAGE1(request):
    return HttpResponse("<html><body bgcolor='#4545ab'>This is page 1</body></html>")

    
def PAGE2(request):
    return HttpResponse("This is page 2")

def home(request):
    data = {
        'c_name':"MPSTME",
        'line1':"Hey",
        'line2': "hey2",
            }
    # return render(request, 'home.html') 
    return render(request, 'home.html', data) 
def showproducts(request):
    data = {
        'products': ['Java', 'python', 'php', 'html'],
        'title': 'languages', 
        'info': [
            {'name':'java','duration':'70H','fees':10},
            {'name':'python','duration':'30H','fees':20},
            {'name':'php','duration':'40H','fees':30},
            {'name':'android','duration':'50H','fees':90},


        ]
    }
    return render(request, 'products.html', data)

def showtest(request):
    return render(request, 'test.html')