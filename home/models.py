from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
  

    def __str__(self):
        return f"{self.title} — {self.author}"


class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="quotes")

    text = models.TextField()
    page_number = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:100]
