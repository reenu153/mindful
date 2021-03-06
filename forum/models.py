from django.db import models
from django.conf import settings

# Create your models here.


class Thread(models.Model):

    title = models.CharField(max_length=500)
    desc = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:10] + ':' +self.thread.title
