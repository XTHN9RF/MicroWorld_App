from django.db import models
from django.conf import settings


class MessageManager(models.Manager):
    def get_messages(user):
        users = []
        messages = Message.objects.filter(user=user).values('recepient').annotate(last=Max('created_at')).order_by('-last')
        for message in messages:
            users.append({
                'user': User.objects.get(pk=message['recepient']),
                'last': message['last'],
                'unread': Message.objects.filter(user=user, recepient__pk=message['recepient'], is_read=False).count()
            })
        return users

    def send_message(self, sender, recepient, message):
        sender_message = Message(
            sender=sender,
            recepient=recepient,
            content=message
        )
        sender_message.save()

        recepient_message = Message(
            sender=sender,
            recepient=recepient,
            content=message
        )
        recepient_message.save()


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.CASCADE)
    recepient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recepient', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    objects = MessageManager()

    def __str__(self):
        return self.content
