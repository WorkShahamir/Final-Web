from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration-popup/', views.registration_popup, name='registration-popup'),
    path('register/', views.register, name='register'),
    path('my_board/', views.my_board_view, name='my_board'),
    path('login/', views.login_view, name='login'),
    path('', views.logout_view, name='logout'),
    path('profil/', views.profil_view, name='profil'),
    path('shop/', views.shop_view, name='shop'),
    path('achivments/', views.achivments_view, name='achivments')
]
