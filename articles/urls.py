from django.urls import path
from .views import index, index_year, index_year_month


urlpatterns = [
    path("", index),
    path("<int:year>", index_year),
    path("<int:year>/<int:month>/", index_year_month),
]
