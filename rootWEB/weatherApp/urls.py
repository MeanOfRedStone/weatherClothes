"""rootWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from weatherApp import views

urlpatterns = [
    #홈페이지 부분
    #메인
    path('main/', views.main, name = 'main'),
    #로그인
    path('login/', views.login),
    #회원가입
    path('join/', views.join),
    #로그아웃
    path('logout/', views.logout),

    #지도-날씨 API 부분
    #검색하면 날씨로 비동기 통신
    path('searchWeather/', views.searchWeather),


]
