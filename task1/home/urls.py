from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.logins,name='login'),
    path('sign-up/',views.SignUp,name='sign-up'),
    path('logout/', views.logout_view, name='logout'),
]
