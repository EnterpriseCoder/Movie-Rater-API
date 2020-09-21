from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=325)

class Rating(models.Model):
    #on_delete if you delete that movie also need to delete rating
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    
    class Meta:
        #if same user votes on same movie more then 1 time it will be rejected
        unique_together = (('user','movie'))
        index_together = (('user','movie'))