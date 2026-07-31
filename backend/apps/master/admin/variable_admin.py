from django.contrib import admin

from apps.master.models import Variable

@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "weight",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "code",
        "name",
    )

    ordering = (
        "code",
    )
