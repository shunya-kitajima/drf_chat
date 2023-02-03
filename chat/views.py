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
