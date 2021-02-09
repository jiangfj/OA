"""oa_behind URL Configuration

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
from django.urls import path, include
from user import views as user_views
from btoken import views as btoken_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/users',user_views.UsersView.as_view()),
    path('v1/btokens',btoken_views.Token_View.as_view()),
    path('v1/users/',include('user.urls')),
    path('v1/notice_list/', include('notice.urls')),
    path('v1/notice_add/', include('notice.urls')),
    path('v1/notice/', include('notice.urls')),
    path('v1/notice_update/', include('notice.urls')),
    path('v1/notice_del/', include('notice.urls')),
    path('v1/report_list/', include('report.urls')),
    path('v1/report_add/', include('report.urls')),
    path('v1/report/', include('report.urls')),
    path('v1/report_update/', include('report.urls')),
    path('v1/report_del/', include('report.urls')),
    path('v1/address/',include('address.urls')),
    path('v1/weather/',include('weather.urls')),
    path('v1/department/', include('department.urls')),
    path('v1/management/', include('management.urls')),
]
