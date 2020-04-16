
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('home/', views.home),
    path('logout/', views.logout_user),
    path('perfil/', views.perfil_user),
    path('registrar/', views.registrar_user),
    path('registrar/submit', views.set_user),
    path('recuperarsenha/', views.recuper_senha_user),


    path('',RedirectView.as_view(url='login/'))

   
]

