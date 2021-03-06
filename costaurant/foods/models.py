from django.db import models

class Menu(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  price = models.IntegerField()
  imgPath = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name