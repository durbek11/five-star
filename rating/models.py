from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class RateStar(models.Model):
    img = models.ImageField(upload_to="image/")
    score = models.IntegerField(default=0,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0),
            ]
    )

    def __str__(self):
        return f"{str(self.pk)}-chi"
