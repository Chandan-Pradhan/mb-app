from django.db import models        #help to build new database models “model”
                                    # the characteristics of the data in our database

# Create your models here.


class Post(models.Model):  # new database model post
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
