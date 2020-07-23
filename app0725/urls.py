from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts', include('allauth.urls')),
    path('', views.create, name="create"),
    path('detail/<int:pk>', views.read, name="detail"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
] 
