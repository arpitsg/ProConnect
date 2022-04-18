from django.contrib import admin

from .models import Connection, Connection_Request
# Register your models here.
class ConnectionAdmin(admin.ModelAdmin):
    model = Connection
    raw_id_fields = ('to_user', 'from_user')


class Connection_RequestAdmin(admin.ModelAdmin):
    model = Connection_Request
    raw_id_fields = ('from_user', 'to_user')


admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Connection_Request, Connection_RequestAdmin)