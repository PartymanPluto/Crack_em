# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:53:00 2019

@author: thero
"""

from django import forms 
from crack_app.models import Recipe, UserProfile, Comment
from django.contrib.auth.models import User

EGG_TYPES = [('omlette', 'An omlette'),
             ('boiled', 'Fried'),
             ('scrambled', 'Scrambled'),
             ('poached', 'Poached'),
             ('sauce/filling', 'Sauce/Filling'),
             ('other', 'something else...')]


class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length = 128, 
                           help_text = 'Please enter the name of your creation!')
    egg_type = forms.CharField(label = 'What sort of egg is your creation?',
                               widget = forms.Select(choices=EGG_TYPES), 
                               required = False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    ratings = forms.IntegerField(widget=forms.HiddenInput(), initial={'0':0, 
                                 '1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,
                                 '8':0,'9':0,'10':0})
    Ingrediants = forms.TextField(help_text = '''Please enter your ingrediants 
                                  in a comma seperated list here in the form of 
                                  "IngrediantA : quantity".''')
    Instructions = forms.TextField(help_text = '''You can enter the instuctions
                                   for your creation here!''')
    
    class Meta:
        model = Recipe
        exclude= ('average_ratings', 'recipe_id')
    
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)  
        
    class Meta:
        model = UserProfile
        fields = ('picture')
    
class CommentForm(forms.ModelForm):
    content = forms.TextField(help_text = '''Tell the chef our thoughts!''')
    
    class Meta:
        model = Comment
        fields = ('user', 'content')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    