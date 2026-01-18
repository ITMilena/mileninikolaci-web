from django.contrib import admin
from django.urls import path
from kolaci import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pocetna, name='pocetna'),
    path('ponuda/', views.ponuda, name='ponuda'),
    path('kontakt/', views.kontakt, name='kontakt'),
]
