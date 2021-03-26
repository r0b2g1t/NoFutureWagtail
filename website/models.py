from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=101)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.first_name} {self.email}"