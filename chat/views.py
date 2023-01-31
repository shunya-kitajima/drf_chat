from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"


class ChatRoom(TemplateView):
    template_name = "chat/chat_box.html"

