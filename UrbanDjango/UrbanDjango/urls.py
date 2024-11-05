"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import task2.views
from task2.views import GetClass
import task3.views
import task4.views
import task5.views

# Для домашнего задания "Базовые HTML теги в шаблонах"

# Если проверяется данное домашнее задание, раскомментировать кода ниже,
# а домашнее задание "DTL. Теги, наследование" оставить закомментированным.

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('get_class/', GetClass.as_view()),
#     path('get_func/', task2.views.get_func),
#     path('platform/', task3.views.platform),
#     path('games/', task3.views.games),
#     path('cart/', task3.views.cart),
#     path('html_sign_up/', task5.views.sign_up_by_html),
#     path('django_sign_up/', task5.views.sign_up_by_django),
# ]



# Для домашнего задания "DTL. Теги, наследование"
# Если проверяется данное домашнее задание, раскомментировать кода ниже,
# а домашнее задание "Базовые HTML теги в шаблонах" оставить закомментированным.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_class/', GetClass.as_view()),
    path('get_func/', task2.views.get_func),
    path('platform/', task4.views.platform),
    path('games/', task4.views.games),
    path('cart/', task4.views.cart),
    path('html_sign_up/', task5.views.sign_up_by_html),
    path('django_sign_up/', task5.views.sign_up_by_django),
]
