from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    
    def __str__(self):
        return self.last_name
    
class Movie(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField()
    director = models.ForeignKey('Person', related_name = 'director', blank = True, null = True)
    actor = models.ManyToManyField('Person', related_name = 'actors')
    year = models.IntegerField()
    
    def actors(self):
        return ', '.join(a.last_name for a in self.actor.all())
    
#     def directors(self):
#         return ','.join(a.last_name for a in self.director.all())
    
    def __str__(self):
        return self.title
