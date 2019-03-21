# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:53:00 2019

@author: thero
"""

from django import forms 
from crack_app.models import Recipe, UserProfile, Comment, Rating
from django.contrib.auth.models import User

EGG_TYPES = [('omlette', 'An omlette'),
             ('fried', 'Fried'),
             ('scrambled', 'Scrambled'),
             ('poached', 'Poached'),
             ('s/f', 'Sauce/Filling'),
             ('other', 'something else...')]

RATINGS = [(1, "(1) Shell-shockingly bad!"), 
           (2, "(2) Hardly egg-ceptional"),
           (3, "(3) "),
           (4, "(4) "),
           (5, "(5) "),
           ]

class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length = 128, 
                           help_text = 'Please enter the name of your creation!')
    egg_type = forms.CharField(label = 'What sort of egg is your creation?',
                               widget = forms.Select(choices=EGG_TYPES), 
                               required = False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    ratings = forms.IntegerField(widget=forms.HiddenInput(), initial={'0':0, 
                                 '1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,
                                 '8':0,'9':0,'10':0})
    ingrediants = forms.CharField(help_text = '''Please enter your ingrediants 
                                  in a comma seperated list here in the form of 
                                  "IngrediantA : quantity".''')
    instructions = forms.CharField(help_text = '''You can enter the instuctions
                                   for your creation here!''')
    
    class Meta:
        model = Recipe
        fields = ('title', 'egg_type', 'views', 'ratings', 'ingrediants', 'instructions')
    
    
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
    content = forms.CharField(help_text = '''Tell the chef our thoughts!''')
    
    class Meta:
        model = Comment
        fields = ('user', 'content')
        
class RatingForm(forms.ModelForm):
    rated = forms.IntegerField(label= 'How did you find this recipe?',
                               widget = forms.Select(choices=RATINGS))
    
    class Meta:
        model = Rating
        fields=('rated',)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    