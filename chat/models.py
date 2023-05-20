from django.db import models
from django.conf import settings


class MessageManager(models.Manager):
    def get_last_10_messages(self, sender, recepient):
        return Message.objects.filter(
            (models.Q(sender=sender) & models.Q(recepient=recepient)) | (models.Q(sender=recepient) & models.Q(recepient=sender))
        ).order_by('-created_at')[:10]

    def send_message(self, sender, recepient, message):
        return Message.objects.create(
            sender=sender,
            recepient=recepient,
            message=message
        )


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    recepient = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    objects = MessageManager()

    def __str__(self):
        return self.message
