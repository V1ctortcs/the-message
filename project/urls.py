
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('themessage/login/', views.login_user),
    path('themessage/login/submit', views.submit_login),
    path('themessage/home/', views.home),
    path('themessage/logout/', views.logout_user),
    path('themessage/perfil/', views.perfil_user),
    path('themessage/registrar/', views.registrar_user),
    path('themessage/registrar/submit', views.set_user),
    path('themessage/recuperarsenha/', views.recuper_senha_user),


    path('',RedirectView.as_view(url='themessage/login/'))

   
]

