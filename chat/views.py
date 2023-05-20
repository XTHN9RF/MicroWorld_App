from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Message

class HomeView(TemplateView):
    template_name = 'chat/index.html'


class InboxView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        messages = Message.objects.get_messages(user=user)
        active_chat = None
        chat = None
        if messages:
            message = messages[0]
            active_chat = message['user'].email
            chat = Message.objects.filter(user=user, recepient=message['user'])
            chat.update(is_read=True)

            for message in messages:
                if message['user'].email == active_chat:
                    message['unread'] = 0

            context = {
                'messages': messages,
                'active_chat': active_chat,
                'chat': chat
            }
            return render(request, 'chat/index.html', context)