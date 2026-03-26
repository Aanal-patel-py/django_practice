from django.contrib import admin
from app1.models import Person,fav_color

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')
    list_filter = ('first_name',)
admin.site.register(Person,PersonAdmin)

@admin.register(fav_color)
class fav_colorAdmin(admin.ModelAdmin):
    list_display=('color','chosen_by')

