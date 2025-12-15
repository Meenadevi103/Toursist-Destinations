from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns=[
        path('',views.login_user,name='login'),
        path('register/',views.register,name='register'),
        
         path('logout/', views.logout_user, name='logout'),
    # path('home/', views.home, name='home'),
    # path('<int:pk>/', views.destination_detail, name='destination_detail'),
    # path('add/', views.destination_create, name='destination_create'),
    # path('<int:pk>/edit/', views.destinaton_update, name='destination_update'),
    # path('<int:pk>/delete/', views.destination_delete, name='destination_delete'),
        path('list/', views.destination_list, name='destination_list'),
    # path('<int:pk>/', views.destination_detail, name='destination_detail'),
        path('add/', views.destination_create, name='destination_create'),
    path('<int:pk>/edit/', views.destinaton_update, name='destination_update'),
    path('<int:pk>/delete/', views.destination_delete, name='destination_delete'),
    
]