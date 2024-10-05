from django.contrib import admin

from startup.portfolio.models import Contact, Experience, Project, Skill

# Register your models here.
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Project)


