import imp
from django.contrib import admin
from all_in_one_cp.models import user_details, platform_details

admin.site.register(user_details)
admin.site.register(platform_details)
