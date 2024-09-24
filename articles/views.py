from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You`re at the articles.index.</h>")


def index_year(request, year):
    if year < 2000:
        return HttpResponse("<h1>Invalid year. Year must be at least 2000.</h1>")
    if year > 2024:
        return HttpResponse("<h1>Invalid year. Year must be no more than 2024.</h1>")
    return HttpResponse(
        f"<h1>Hello, world. You`re at the articles.index_year: {year}.</h1>"
    )


def index_year_month(request, month):
    return HttpResponse("<h1>Hello")
