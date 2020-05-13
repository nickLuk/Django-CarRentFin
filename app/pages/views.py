from django.shortcuts import render

from cars.models import CarsList
from carmanager.models import CarManager
from .cars_Info import vendor_list, models_list, engine_list, transmission_list

def index(request):

    cars = CarsList.objects.all().filter(is_published=True)
    query = CarsList.objects.order_by("vendor")
    random_car = CarsList.objects.order_by('?')[0]

    if "vendor" in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)

    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)

    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)

    if "transmission" in request.GET:
        transmission = request.GET["transmission"]
        if transmission:
            query = query.filter(transmission__iexact=transmission)

    context = {
        "vendor_list": vendor_list,
        "models_list": models_list,
        "engine_list": engine_list,
        "transmission_list":transmission_list,
        "cars": query,
        "request_value": request.GET,
        "random_car":random_car
    }

    

    return render(request, 'pages/index.html', context)


def about(request):
    managers = CarManager.objects.all().filter(visible=True)[:6]

    context = {
        'managers': managers,
        'title': "About Us",

    }
   
    return render(request, 'pages/about.html', context)


def blog(request):
    
    context = {
        'title': "Car Articles",

    }
   
    return render(request, 'pages/blog.html', context)


def services(request):
    data = {'title': "Our Services"}
    return render(request, 'pages/services.html', data)


def contactus(request):
    data = {'title': "Contact Us"}
    return render(request, 'pages/contactus.html', data)

def search(request):
    query = CarsList.objects.order_by("vendor")

    if "vendor" in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)

    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)

    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)

    if "transmission" in request.GET:
        transmission = request.GET["transmission"]
        if transmission:
            query = query.filter(transmission__iexact=transmission)

    context = {
        "vendor_list": vendor_list,
        "models_list": models_list,
        "engine_list": engine_list,
        "transmission_list":transmission_list,
        "cars": query,
        "request_value": request.GET
    }

    return render(request, 'pages/search.html', context)