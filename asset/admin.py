#encoding: utf-8

from django.contrib import admin

from .models import Host
from .forms import HostForm

admin.site.site_title = 'CMDB'
admin.site.site_header = 'CMDB'

class HotAdmin(admin.ModelAdmin):
    form = HostForm
    list_display = ['name', 'ip', 'mem', 'cpu', 'os', 'arch', 'created_time', 'is_online']
    date_hierarchy = 'created_time'
    search_fields = ['name', 'ip', 'remark']
    list_filter = ['os', 'arch', 'cpu', 'mem']


admin.site.register(Host, HotAdmin)