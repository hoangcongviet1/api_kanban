from django.contrib import admin
from .models import userData, workSpace, column, card

# Register your models here.

admin.site.register(userData)
admin.site.register(workSpace)
admin.site.register(column)
admin.site.register(card)

