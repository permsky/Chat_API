from django.contrib import admin
from .models import User, Chat, Message


admin.site.register((User, Chat, Message))
