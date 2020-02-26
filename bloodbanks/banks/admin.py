from django.contrib import admin

from .models import State, BloodBank, BloodGroup, BloodBag, Size, TotalBlood

# Register your models here.
admin.site.register(State)
admin.site.register(BloodGroup)
admin.site.register(BloodBank)
admin.site.register(BloodBag)
admin.site.register(Size)
admin.site.register(TotalBlood)


