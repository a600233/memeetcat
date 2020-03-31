from django.urls import path
from yumiao import views

app_name = 'yumiao'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('forgot/', views.forgot, name='forgot'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('forum/', views.forum, name='forum'),
    path('contact/', views.contact, name='contact'),
    path('model/', views.model, name='model'),
    path('model_apply/', views.model_apply, name='model_apply'),
    path('model_details/', views.model_details, name='model_details'),
    path('model_change/', views.model_change, name='model_change'),
]