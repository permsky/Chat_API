from django.db import models


class User(models.Model):
    username = models.CharField(
        max_length=30,
        verbose_name='Имя пользователя',
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания пользователя'
    )

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
    
    def __str__(self):
        return f'Пользователь {self.username}'


class Chat(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя чата',
        unique=True
    )
    users = models.ManyToManyField(User, verbose_name='Пользователи в чате')
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания чата'
    )

    class Meta:
        verbose_name_plural = 'Чаты'
        verbose_name = 'Чат'
    
    def __str__(self):
        return f'Чат {self.name}'


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        verbose_name='Чат'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    text = models.TextField(
        max_length=1000,
        verbose_name='Текст сообщения'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания сообщения'
    )

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
    
    def __str__(self):
        return f'Сообщение пользователя {self.author} от {self.created_at}'
