from rest_framework import generics
from rest_framework.response import Response

from .models import Chat, Message, User
from .serializers import (
    UserSerializer,
    ChatSerializer,
    MessageSerializer
)


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self,request):
        user = User.objects.create(username=self.request.data.get('username'))
        return Response({'id': user.id})


class CreateChatAPIView(generics.CreateAPIView):
    serializer_class = ChatSerializer

    def post(self,request):
        chat = Chat.objects.create(
            name=self.request.data.get('name'),
        )
        chat.users.set(self.request.data.get('users'))
        return Response({'id': chat.id})


class CreateMessageAPIView(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def post(self,request):
        message = Message.objects.create(
            chat=Chat.objects.get(id=self.request.data.get('chat')),
            author=User.objects.get(id=self.request.data.get('author')),
            text=self.request.data.get('text')
        )
        return Response({'id': message.id})


class GetChatsAPIView(generics.ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id = self.request.data.get('user')
        chats = Chat.objects.filter(users__id=user_id)
        chat_ids = chats.order_by('-message__created_at').values('id')
        unique_chat_ids = list()
        for number, chat_id in enumerate(chat_ids):
            if chat_ids[number] not in unique_chat_ids:
                unique_chat_ids.append(chat_ids[number]) 
        chats = list()
        for chat_id in unique_chat_ids:
            chats.append(Chat.objects.get(id=chat_id['id']))
        return chats

    def post(self,request):
        chats = self.get_queryset()
        serializer = self.serializer_class(chats, many=True)
        return Response(serializer.data)


class GetMessagesAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        chat_id = self.request.data.get('chat')
        return Message.objects.filter(chat=chat_id).order_by('created_at')

    def post(self,request):
        messages = self.get_queryset()
        serializer = self.serializer_class(messages, many=True)
        return Response(serializer.data)
