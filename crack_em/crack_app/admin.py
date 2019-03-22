from django.contrib import admin
from crack_app.models import Egg, Recipe, UserProfile

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'egg_type')
    prepopulated_fields = {'slug': ('title',)}
    
class EggAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Egg, EggAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserProfile)
