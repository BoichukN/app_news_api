from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from posts.models import Post


class Comment(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        unique_together = ['author', 'content', 'created']

    def __str__(self):
        return f'{self.content} from {self.author} created at {self.created}.'

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
