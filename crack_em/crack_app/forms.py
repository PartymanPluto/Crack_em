# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:53:00 2019

@author: thero
"""

from django import forms 
from crack_app.models import Egg, Recipe, UserProfile, Comment, Rating
from django.contrib.auth.models import User

Omlette = Egg.objects.filter(title ='Omlette')
Fried = Egg.objects.get(title ='Fried')
Scrambled = Egg.objects.get(title='Scrambled')
Poached =Egg.objects.get(title ='Poached')
Sauces = Egg.objects.get(title ='Sauces/Fillings')
Other = Egg.objects.get(title = 'Other')

EGG_TYPES = [(Omlette, 'An omlette'),
             (Fried, 'Fried'),
             (Scrambled, 'Scrambled'),
             (Poached, 'Poached'),
             (Sauces, 'Sauce/Filling'),
             (Other, 'something else...')]

RATINGS = [(1, "(1) Shell-shockingly bad!"), 
           (2, "(2) Hardly egg-ceptional"),
           (3, "(3) Just your everyday yolk"),
           (4, "(4) An eggsemplary recipe!"),
           (5, "(5) Simply eggcellent!"),
           ]

class EggForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    
    class Meta:
        model = Egg
        fields = ('title',)
        
class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length = 128, 
                           help_text = 'Please enter the name of your creation!')
    et = forms.CharField(help_text = 'What sort of egg is your creation?',
                               label = 'What sort of egg is your creation?',
                               widget = forms.Select(choices=EGG_TYPES), 
                               required = True)
    image = forms.ImageField(help_text = 'What does your masterpiece look like?',
                             required = False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    ingrediants = forms.CharField(help_text = '''Please enter your ingrediants 
                                  in a comma seperated list here in the form of 
                                  "IngrediantA : quantity".''')
    instructions = forms.CharField(help_text = '''You can enter the instuctions
                                   for your creation here! Leave a semi colon 
                                   to indicate the end of a step and if any 
                                   preparation is need write it as a step with
                                   Prep: at the start.''')
    
    class Meta:
        model = Recipe
        fields = ('title', 'egg_type', 'image', 'views', 'ingrediants', 'instructions')
    
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
        
    class Meta:
        model = UserProfile
        fields = ('picture',)
    
class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length = 512,)
    
    class Meta:
        model = Comment
        fields = ('content',)
        
class RatingForm(forms.ModelForm):
    rated = forms.IntegerField(label= 'How did you find this recipe?',
                               widget = forms.Select(choices=RATINGS))
    
    class Meta:
        model = Rating
        fields=('rated',)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    