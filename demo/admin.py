from django.contrib import admin

# Register your models here.

    
from demo.models import Project, Blog, Team , Contact , Course

admin.site.register(Project)

admin.site.register(Blog)
admin.site.register(Team)

admin.site.register(Contact)

admin.site.register(Course)
