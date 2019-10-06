from django.contrib import admin
from .models import CompInfo, Area, CompClass,test11, BBSSection
# Register your models here.
# test1
@admin.register(CompInfo)
class CompInfoAdmin(admin.ModelAdmin):
     list_display = ('IName',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('Name',)

@admin.register(CompClass)
class CompClassAdmin(admin.ModelAdmin):
    list_display = ('CName',)

@admin.register(BBSSection)
class CompClassAdmin(admin.ModelAdmin):
    list_display = ('SName',)

@admin.register(test11)
class testAdmin(admin.ModelAdmin):
    list_display = ('name',)

# admin.site.register(CompInfo)
# admin.site.register(Area)