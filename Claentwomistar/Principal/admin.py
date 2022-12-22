from django.contrib import admin
from Administracion.models import Productos,DetalleProductos
# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nombre']
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('Valor','Stock','Ventas')}
            ),
        )
class DetalleProductosAdmin(admin.ModelAdmin):
    list_display = ['id', 'Marca']
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('Marca', 'Descripcion','Modelo')}
            ),
        )
admin.site.register(Productos, ProductosAdmin)
admin.site.register(DetalleProductos, DetalleProductosAdmin)