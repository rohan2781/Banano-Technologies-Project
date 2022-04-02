from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.logins,name='login'),
    path('sign-up/',views.SignUp,name='sign-up'),
    path('add-blog/',views.add_blog,name='add-blog'),
    path('appointment/<str:id>',views.book,name='book'),
    path('book/<str:id>',views.appoint,name='appoint'),
    path('logout/', views.logout_view, name='logout'),
    path('account/<str:id>',views.client,name='client'),
    path('view/<str:id>',views.show,name='show'),
    path('booked/<str:id>',views.done,name='done'),
]
