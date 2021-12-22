from django.contrib import admin
from .models import *

admin.site.site_header = 'Lyon Palme Entrainement'


class AdherentAdmin(admin.ModelAdmin):
    # ...
    editable_list = ['Prenom']


class EntrainementAdmin(admin.ModelAdmin):
    list_display = ("Dates", "coach")


@admin.register(Entraineur)
class EntraineurAdmin(admin.ModelAdmin):
    search_fields = ("Prenom__startswith", "Nom__startswith")


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    search_fields = ("Prenom__startswith", "Nom__startswith")


@admin.register(Adherent)
class AdherentAdmin(admin.ModelAdmin):
    search_fields = ("Prenom__startswith", "Nom__startswith")


@admin.register(Entrainement)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("Dates", "coach")
    list_filter = ("Dates",)


admin.site.register(Role)


class ProjectAdmin(admin.ModelAdmin):
    # ...
    search_fields = ('name',)
