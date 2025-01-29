from django.contrib import admin
from django.urls import path, include
from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', include('social_django.urls', namespace='social')),
]