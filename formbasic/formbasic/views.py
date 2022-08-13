#HttpResponseRedirect is for redirecting the page after submiting 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 

def myform(request):
    add = 0
    n1=0
    n2=0
    try:
        if(request.POST):
            # n1 = int(request.POST['t1'])
            n1 = int(request.POST.get('t1'))

            # n2 = int(request.POST['t2'])
            n2 = int(request.POST.get('t2'))
            add = n1 + n2
            return HttpResponseRedirect('/resultpage')

    except:
        pass
    return render(request, "myform.html", {'n1':n1, 'n2':n2, 'add': add})

def resultpage(request):
    return HttpResponse("result page")