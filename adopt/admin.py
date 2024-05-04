from django.contrib import admin
from .models import User, Pet, Comment, Organization

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Pet)
admin.site.register(Comment)

