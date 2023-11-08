from django.db import models

# Create your models here.

class Strategy(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = "Strategy"

    