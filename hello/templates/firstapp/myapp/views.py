from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from .forms import UserForm
# from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
#from googlesearch import search
# from django.http import *
from django.template.response import TemplateResponse
#from .models import Person


# Create your views here.


def index(request):
#    people = Person.object.all()
    return HttpResponse('''<h1>Main page</h1>
<hr>
This is my super project in django
''')

