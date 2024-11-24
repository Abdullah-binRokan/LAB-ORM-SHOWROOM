from django.shortcuts import render, redirect
from django.http import HttpRequest
from brands.models import Brand
from .models import Car, Color
from .forms import CarForm


# Create your views here.
def all_cars_view(request: HttpRequest):

    return render(request, "cars/all.html")


def add_car_view(request: HttpRequest):
    brands = Brand.objects.all()
    colors = Color.objects.all()
    context = {"brands": brands, "colors": colors}

    if request.method == "POST":
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect("main:home_view")
        else:
            print("form error: ", car_form.errors)

    return render(request, "cars/add.html", context)