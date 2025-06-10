from django.contrib import admin

from .models import (
    Armaduras,
    Armas,
    Ataque,
    CaArmadura,
    Ficha,
    ListaMagia,
    Magias,
    Pericias,
    Usuario,
)

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ficha)
admin.site.register(Pericias)
admin.site.register(ListaMagia)
admin.site.register(Magias)
admin.site.register(Armaduras)
admin.site.register(CaArmadura)
admin.site.register(Armas)
admin.site.register(Ataque)
