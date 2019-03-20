from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    SCRAMBLED = 'scrambled'
    BOILED = 'boiled'
    FRIED = 'fried'
    POACHED = 'poached'
    OTHER = 'other'
    EGG_CHOICES = (
        (SCRAMBLED, 'Scrambled'),
        (BOILED, 'Boiled'),
        (FRIED, 'Fried'),
        (POACHED, 'Poached'),
        (OTHER, 'Other'),
    )
    
    egg_type = models.CharField(
        choices = EGG_CHOICES,
        default = SCRAMBLED        
    )
    
    def egg_selected(self):
        return self.egg_type
    
    
    
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 128)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', default = null)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural =  'pages'
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length = 512)
    
#Not sure if this is needed
class user(models.model):
    profile_pic = models.FileField(upload_to='uploads/%Y/%m/%d/', default = null)
    name = models.CharField(max_length = 128)
    
    
    
