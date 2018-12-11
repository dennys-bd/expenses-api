"""expenses URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from accounts.api.v1.viewsets import AccountViewSet
from cards.api.v1.viewsets import CardViewSet
from incomings.api.v1.viewsets import IncomingViewSet
from shoppings.api.v1.viewsets import CategoryViewSet, ShoppingViewSet, InstallmentViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet, base_name='Account')
router.register(r'cards', CardViewSet, base_name='Card')
router.register(r'incomings', IncomingViewSet, base_name='Incoming')
router.register(r'categories', CategoryViewSet, base_name='Category')
router.register(r'shoppings', ShoppingViewSet, base_name='Shopping')
router.register(r'installments', InstallmentViewSet, base_name='Installment')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^api-token-auth/', obtain_jwt_token),
]
