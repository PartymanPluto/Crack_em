from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Egg(models.Model):  
    title = models.CharField(max_length = 128, unique = True)
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Egg, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    
    
class Recipe(models.Model):
    egg_type = models.ForeignKey(Egg)
    title = models.CharField(max_length = 128)
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to='recipe_images', default = None)
    ingrediants = models.CharField(max_length = 512)
    instructions = models.CharField(max_length = 2048)
    views = models.IntegerField(default=0)
    average_rating = models.IntegerField(default=0)
    slug = models.SlugField(max_length = 128, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural =  'recipes'
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.CharField(max_length = 512)
    recipe = models.ForeignKey(Recipe)
    
    def __str__(self):
        return self.content
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    rated = models.ManyToManyField(Recipe, blank=True)
    likes = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.user.username
    
class Rating(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
    rated = models.IntegerField()
    
