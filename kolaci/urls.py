from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ponuda/', views.ponuda, name='ponuda'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('o-nama/', views.onama, name='onama'),
    path("cenovnik/", views.cenovnik, name="cenovnik"),

]
