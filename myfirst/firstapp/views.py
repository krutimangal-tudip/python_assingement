
from django.http import HttpResponse, HttpResponseNotFound
from .models import Student
from django.shortcuts import render
from firstapp.models import Student
#from firstapp.forms import Name
from firstapp.forms import YourLoginForm

'''def hello(request):

    return render(request, 'x.html')


def hello_save(request):


    if request.method == "POST":
        a1= Name(request.POST, request.POST)
        if a1.is_valid():

            a2= Student()
            a2.first_name= a1.cleaned_data["first_name"]
            a2.last_name = a1.cleaned_data["last_name"]
            a2.save()
            saved  = True

    else:
        a1= Name




    return render(request, 'y.html',locals())'''

def hello(request):

    return render(request, 'z.html', {"YourLoginForm": YourLoginForm})





