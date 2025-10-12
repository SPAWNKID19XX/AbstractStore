from django.contrib import admin
from .models import CustomUser

# Register your models here.
class AdminCustomUser(admin.ModelAdmin):
    list_display = ["email", "full_name", "is_active","is_staff","is_superuser"]

    @admin.display(empty_value="???")
    def view_birth_date(self, obj):
        return obj.email


admin.site.register(CustomUser, AdminCustomUser)