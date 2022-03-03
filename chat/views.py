from rest_framework import generics
from rest_framework.response import Response

from .models import Chat, Message
from .serializers import (
    UserSerializer,
    ChatSerializer,
    MessageSerializer
)


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateChatAPIView(generics.CreateAPIView):
    serializer_class = ChatSerializer


class CreateMessageAPIView(generics.CreateAPIView):
    serializer_class = MessageSerializer


class GetChatsAPIView(generics.ListCreateAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id = self.request.data.get('user')
        return Chat.objects.filter(users__id=user_id).order_by('-created_at')

    def post(self,request):
        chats = self.get_queryset()
        serializer = self.serializer_class(chats, many=True)
        return Response({'chats': serializer.data})


class GetMessagesAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        chat_id = self.request.data.get('chat')
        return Message.objects.filter(chat=chat_id).order_by('created_at')

    def post(self,request):
        messages = self.get_queryset()
        serializer = self.serializer_class(messages, many=True)
        return Response({'messages': serializer.data})
