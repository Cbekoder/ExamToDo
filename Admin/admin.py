from django.contrib import admin

from .models import *

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'name', 'age', 'course']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    search_help_text = 'Ism bo\'yicha qidiring'
    list_filter = ['course']

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'student_fk', 'sana', 'done']
    list_display_links = ['id', 'title']
    list_filter = ['done']
    search_fields = ['title']
    search_help_text = 'Sarlavha bo\'yicha qidiring'
    autocomplete_fields = ['student_fk']


# admin.site.register(Author)
# admin.site.register(Plan)
