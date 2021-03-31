from django.contrib import admin
from api_messages.models import Message
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'body']