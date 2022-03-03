"""test_1 URL Configuration

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
from django.urls import path

from chat import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/add', views.CreateUserAPIView.as_view(), name='add_user'),
    path('chats/add', views.CreateChatAPIView.as_view(), name='add_chat'),
    path('messages/add', views.CreateMessageAPIView.as_view(), name='add_messages'),
    path('chats/get/', views.GetChatsAPIView.as_view(), name='user_chats'),
    path('messages/get/', views.GetMessagesAPIView.as_view(), name='chat_messages'),
]
