from django.shortcuts import render
from .forms import UserForm
# from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse

# from django.http import *
from django.template.response import TemplateResponse
from .models import Person


# Create your views here.

# функция запроса инфы из базы данных и загрузка индексного файла хтмл с этими данными в браузер пользователя
def index(request):
    people = Person.object.all()
    return render(request,"index.html", {"people" : people})
    # if request.method == "POST":
    #     name = request.POST.get ("name") # получить значение поля Имя
    #     age = request.POST.get("age")  # получить значение поля Возраст
    #     output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1} </hЗ>".format(name, age)
    #     return HttpResponse(output)
    # else:
    #     userform = UserForm()
    #     return render(request, "firstapp/index.html", {"form": userform})
    # header = "Персональные данные"  # обычная переменная
    # langs = ["Английский", "Немецкий", "Испанский"]  # массив
    # user = {"name": "Мурат,", "age": 50}  # словарь
    # addr = ("Широкая", 23, 45)  # кортеж
    # data = {"header": header, "langs": langs, "user": user, "address": addr}
    # return render(request, "index.html", context=data)
    # cat = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
    # cat = []
    # userform = UserForm()
    # return render(request,"firstapp/index.html", {"form": userform})

def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")

def delete(request, id):
    try:
        person = Person.object.get(id = id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Нет такого клиента</h2>")

def edit(request, id):
    try:
        person = Person.object.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиeнт не найден</h2>")

# def home(request):
#     return render(request, "home.html")

def about(request):
     return HttpResponse('''<h1>О сервисе</h1>
     <hr>
     Библиотечная база данных''')
    #return HttpResponseNotFound()


def contact(request):
    return HttpResponse('''<h1>Контакты разработчика</h1> 
    <hr>
    Кябишев М.М. http://adawada.ru''')

def products(request, product_id = 1):
    output = "Продукт № {0}".format(product_id)
    return HttpResponse(output)

def users(request, id = '1', user_name = 'Вася'):
    output = "Пользователь № {0} с именем {1}".format(id, user_name)
    return HttpResponse(output)

