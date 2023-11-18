from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    createddate = models.DateTimeField(
        auto_now_add=True, db_column='createddate')
    updateddate = models.DateTimeField(auto_now=True, db_column='updateddate')

    class Meta:
        abstract = True


class Strategy(TimeStampedModel):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = "Strategy"

# class NetPosition(models.Model):


    