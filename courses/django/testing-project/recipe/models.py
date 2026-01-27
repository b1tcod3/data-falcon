from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=['name', 'ingredients','instructions'])]
