from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField(unique=True)
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.link

    @property
    def comments(self):
        instance = self
        from comments.models import Comment
        qs = Comment.objects.filter_by_instance(instance)
        return qs
