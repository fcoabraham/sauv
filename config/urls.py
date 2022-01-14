"""sauv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('admin/', admin.site.urls),
  #path('', admin.site.urls),
  ##path('', login,{'template_name':'index.html'},name='login'),
  #path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
 #path('materias/',include('materias.urls'), name='materias'),
 path('materias/',include(('materias.urls','materias'), namespace='materias')),
 path('', include('django.contrib.auth.urls')),
 #path('',include('materias.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
