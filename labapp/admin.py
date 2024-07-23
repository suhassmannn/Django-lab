from django.contrib import admin
from labapp.models import course, projectReg, student

admin.site.site_header='FDP ON Django'
admin.site.site_title='FDP ON Django'

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('usn','name')
    ordering=('usn',)
    search_fields=('name',)

@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display=('courseCode','courseName')
    ordering=('courseCode',)
    search_fields=('courseName',)

@admin.register(projectReg)
class projectAdmin(admin.ModelAdmin):
    list_display = ['student','ptitle']
    search_fields = ['student',]