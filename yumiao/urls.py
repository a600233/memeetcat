from django.urls import path
from yumiao import views

app_name = 'yumiao'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forgot/', views.forgot, name='forgot'),

]