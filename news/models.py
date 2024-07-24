from datetime import date
from django.db import models
from django.forms import ValidationError

from news.utils.validators import validate_title


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    role = models.CharField(
        max_length=200, null=False, blank=False, default="default_role"
    )

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, blank=False, validators=[validate_title]
    )
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="news")

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
