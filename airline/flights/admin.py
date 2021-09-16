from django.contrib import admin

# Register your models here.

from .models import Airport,Flight

class AirportAdmin(admin.ModelAdmin):
    list_display = ("code", "city")


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

'''
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)'''

admin.site.register(Airport , AirportAdmin)
admin.site.register(Flight)
#admin.site.register(Passenger , PassengerAdmin)










