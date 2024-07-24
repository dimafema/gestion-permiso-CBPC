from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Zona)
admin.site.register(Parque)
admin.site.register(Brigada)
admin.site.register(Usuario)
admin.site.register(Vacaciones)


title = "Panel de gestión de permisos"
subtitle = "Bienvenido al panel de gestión de permisos"
admin.site.site_header = title
admin.site.site_title = title   
admin.site.index_title = subtitle