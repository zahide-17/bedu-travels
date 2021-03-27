from django.contrib import admin
from .models import User,Zona,Tour,Salida

class UserAdmin(admin.ModelAdmin):
    #Se sobre escribe lo que hace __str__
    list_display = ("id","nombre","apellidos","email","fechaNacimiento","genero","tipo")

class ZonaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","descripcion","latitud","longitud")

class TourAdmin(admin.ModelAdmin):
    #Se sobre escribe lo que hace __str__
    list_display = ("id","nombre","slug","operador","tipoDeTour",
                    "descripcion","pais","zonaSalida","zonaLlegada")

class SalidaAdmin(admin.ModelAdmin):
    list_display = ("id","fechaInicio","fechaFin","asientos","precio","tour")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Zona, ZonaAdmin) 
admin.site.register(Tour, TourAdmin)
admin.site.register(Salida, SalidaAdmin)