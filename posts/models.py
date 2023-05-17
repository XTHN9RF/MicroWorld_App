from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Post(models.Model):
    """A blog post model with slug field"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=100, blank=True)
    image = models.ImageField(upload_to='posts/%y/%m/%d', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked', blank=True)

    def __str__(self):
        """Return a string representation of the model title in admin panel"""
        return self.title

    def save(self, *args, **kwargs):
        """Override the save method to auto-generate a slug field"""
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """A blog comment model"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model content in admin panel"""
        return self.content