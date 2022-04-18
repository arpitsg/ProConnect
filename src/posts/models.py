# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models import Count
# from django.db.models.signals import post_delete

# from .signals import delete_pic

# from PIL import Image


# class PostManager(models.Manager):

#     def get_posts(self, status):
#         return self.get_queryset().annotate(
#             num_comments=Count("comment")).filter(archived=status)


# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=150)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     img = models.ImageField(upload_to="post_imgs", blank=True, null=True)
#     description = models.TextField()
#     likes = models.ManyToManyField(User, related_name="likes")
#     archived = models.BooleanField(default=False)

#     objects = PostManager()

#     def __str__(self):
#         return f"{self.user} : {self.title}"

#     class Meta:
#         ordering = ['-created']

#     def save(self):
#         super().save()
#         if self.img:
#             img = Image.open(self.img.path)

#             if img.height > 300 or img.width > 300:
#                 output_size = (600, 600)
#                 img.thumbnail(output_size)
#                 img.save(self.img.path)


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     commented_time = models.DateTimeField(auto_now_add=True, auto_now=False)
#     comment = models.CharField(max_length=250)


# post_delete.connect(delete_pic, Post)

from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile
# Create your models here.

class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='posts', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ['-created',]

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"