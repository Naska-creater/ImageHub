from django.db import models

from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    file = models.ImageField(upload_to='image/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.description
