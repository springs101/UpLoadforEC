"""UpLoadxls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include,url
from chandleExcel import views as chandle_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chandle/showpage', chandle_views.showpage),
    url(r'^chandle/getExcel_tuijian', chandle_views.getExcel_tuijian),
    url(r'^chandle/getExcel_zhitongche', chandle_views.getExcel_zhitongche),
    url(r'^chandle/getExcel_zzdanpin', chandle_views.getExcel_zzdanpin),
    url(r'^chandle/getExcel_zzquandian', chandle_views.getExcel_zzquandian),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
