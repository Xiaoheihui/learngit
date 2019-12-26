from django.contrib import admin
from .models import CompInfo, Area, CompClass,test11, BBSSection, CompRecord, MarkMessage, UserMessage, BBSTopic, BBSReply
# Register your models here.
# test1
@admin.register(CompInfo)
class CompInfoAdmin(admin.ModelAdmin):
     list_display = ('IName', 'Iid')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('Name',)

@admin.register(CompClass)
class CompClassAdmin(admin.ModelAdmin):
    list_display = ('CName',)

@admin.register(BBSSection)
class CompClassAdmin(admin.ModelAdmin):
    list_display = ('SName',)

@admin.register(CompRecord)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('RTitle', 'RID')

@admin.register(MarkMessage)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('CompRecordId', 'UsersId')

@admin.register(UserMessage)
class UserAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'Unickname', 'USex', 'UBirthday')

@admin.register(BBSTopic)
class TopicAdmin(admin.ModelAdmin):
    ordering = ('Tid',)
    list_display = ('Tid', 'TUid', 'TTopic', 'TSid', 'TClickCount', 'TTime')

@admin.register(BBSReply)
class ReplyAdmin(admin.ModelAdmin):
    ordering = ('Rid',)
    list_display = ('Rid', 'RUid', 'RTid', 'RSid', 'RContent', 'RTime')

admin.site.site_header = '大学生赛事平台后台管理'
admin.site.site_title = '大学生赛事平台后台'
