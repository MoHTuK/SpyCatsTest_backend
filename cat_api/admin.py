from django.contrib import admin
from .models import Cat, Mission, Target


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'years_of_exp')


class TargetInline(admin.TabularInline):
    model = Target
    extra = 1


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'complete')
    inlines = [TargetInline]


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'notes', 'complete', 'mission')