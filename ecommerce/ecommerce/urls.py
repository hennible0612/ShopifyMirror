"""ecommerce URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static #MEDIA_URL을 위힌 static 함수 import
from django.conf import settings #setting 에 정의한 MEDIA_URL을 가져옴
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))

]

#MEDIA_URL을 MEDIA_ROOT로 설정해준다
#exampe     /images/Headphones.jpg
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
