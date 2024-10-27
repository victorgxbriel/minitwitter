from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    following = models.ManyToManyField(
        'self',
        through='Follow',
        symmetrical=False,
        related_name='followers'
    )

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follower = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            related_name='following_relations'
        )
    following = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            related_name='follower_relations'
        )
    created_at = models.DateTimeField(auto_now_add=True)
