"""
URL configuration for reservations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from calend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('User/', include('User.urls')),
    path('Administrator/',include('Administrator.urls')),
    path('calendar/', views.index, name='index'), 
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('',views.Home,name='home'),
    path('About/',views.About,name='about'),
    path('Contact/',views.Contact,name='contact'),
    path('Login/',views.Login,name='login'),
    path('Logout/',views.Logout, name='logout'),
    path('Register/',views.Register,name='register'),
    path('Reserver/',views.ReservationCreate,name='reserver'),
]
