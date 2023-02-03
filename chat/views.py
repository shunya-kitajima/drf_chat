from django.shortcuts import render, redirect
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


def add_friend(request, username):
    login_user = request.user
    friend = CustomUser.objects.get(username=username)
    current_user = CustomUser.objects.get(username=login_user)
    friend_lists = current_user.user_friends.all()
    flag = 0
    for friend_list in friend_lists:
        if friend_list.friend.pk == friend.pk:
            flag = 1
            break
    if flag == 0:
        current_user.user_friends.create(friend=friend)
        friend.user_friends.create(friend=current_user)
    return redirect("chat:search_user")


class Home(TemplateView):
    template_name = "home.html"


class ChatRoom(TemplateView):
    template_name = "chat/chat_box.html"


class SearchUser(TemplateView):
    def get(self, request, *args, **kwargs):
        if "search" in self.request.GET:
            query = request.GET.get("search")
            users = list(CustomUser.objects.all())
            user_list = []
            for user in users:
                if query in user.username and user.username != request.user.username:
                    user_list.append(user)
        else:
            user_list = list(CustomUser.objects.all())
            for user in user_list:
                if user.username == request.user.username:
                    user_list.remove(user)
                    break

        friends = get_friends_list(request.user.username)
        return render(request, "chat/search.html", {"users": user_list, "friends": friends})
