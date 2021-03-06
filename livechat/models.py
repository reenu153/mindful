from django.db import models
from django.conf import settings


class ChatRoom(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.username + ':' + self.doctor.username

    class Meta:
        unique_together = ('patient', 'doctor')


class Chat(models.Model):

    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=500)

class Note(models.Model):

    note = models.CharField(max_length=500)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)