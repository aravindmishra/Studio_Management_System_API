"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from customer import views as customerViews
from orders import views as orderViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/add', customerViews.CreateCustomer.as_view()),
    path('order/add', orderViews.CreateOrder.as_view()),
    path('order/update', orderViews.UpdateOrder.as_view()),
    path('order/list', orderViews.OrderList.as_view()),
]
