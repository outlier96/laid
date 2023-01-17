from django.contrib import admin
from .models import User

# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('fname','lname', 'email','password', 'tel')
	ordering = ('fname',)
	search_fields = ('fname', 'lname')
