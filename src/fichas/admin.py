from django.contrib import admin

from .models import Usuario,Ficha,Pericias,ListaMagia,Magias,Armaduras,CaArmadura,Ataque,Armas

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