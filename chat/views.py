from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from accounts.models import CustomUser


def get_friends_list(username):
    try:
        user = CustomUser.objects.get(username=username)
        friends = list(user.user_friends.all())
        return friends
    except friends:
        return []


class Home(TemplateView):
    template_name = "home.html"


class ChatRoom(TemplateView):
    template_name = "chat/chat_box.html"


class SearchUser(TemplateView):

