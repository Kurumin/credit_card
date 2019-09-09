"""credit_card URL Configuration

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
from rest_framework import routers
from credit_card.api.viewsets import ClientViewSet, CardViewSet
from credit_card.views import home, clients, client_detail, cards

router = routers.DefaultRouter()
router.register(r'clients/(?P<client>[\d]+)/cards', CardViewSet)
router.register(r'clients', ClientViewSet)



urlpatterns = [
    path('', home, name='home'),
    path('clients/', clients, name='clients'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('clients/<int:pk>/', client_detail, name='client_detail'),
    path('clients/<int:client_id>/cards/', cards, name='cards'),

]
