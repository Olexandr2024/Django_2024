from django.shortcuts import render
from .models import Category, Dish, Event, Chef, Staff, Gallery, Contacts

# Create your views here.


def index(request):
    categories = Category.objects.filter(is_visible=True).order_by("sort")

    return render(request, "base.html")
