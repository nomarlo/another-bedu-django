from django.contrib import admin

from todo_list.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "name")


admin.site.register(ToDo, ToDoAdmin)

