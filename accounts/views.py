from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("chat:chat_room")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
