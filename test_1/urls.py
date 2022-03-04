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
