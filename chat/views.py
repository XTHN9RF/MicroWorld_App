from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain
from operator import attrgetter

from .forms import MessageForm

from .models import Message
from user.models import User


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


class MessageView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        active_chat = pk

        message_form = MessageForm()

        messages = Message.objects.get_messages(user=user)
        messages_from_user = Message.objects.filter(sender__email=pk, recepient=user)
        messages_to_user = Message.objects.filter(sender=user, recepient__email=pk)
        chat = sorted(chain(messages_from_user, messages_to_user), key=attrgetter('created_at'))

        for message in messages:
            if message['user'].email == active_chat:
                message['unread'] = 0
        context = {
            'messages': messages,
            'active_chat': active_chat,
            'chat': chat,
            'message_form': message_form,
        }
        return render(request, 'chat/messages.html', context)

    def post(self, request, pk):
        user = request.user
        recepient = User.objects.get(email=pk)

        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.user = user
            message.sender = user
            message.recepient = recepient
            message.save()
            return redirect('chat:message', pk=pk)
        else:
            return redirect('chat:message', pk=pk)
