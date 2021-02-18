from django.contrib import admin
from dosxangos.normas.models import *

class NormaAdmin(admin.ModelAdmin):
    model=Norma

admin.site.register(Norma,NormaAdmin)


# Register your models here.
