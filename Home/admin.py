from django.contrib import admin
from .models import (CreateYourTourStyle, DiscoverNewHorizon, OurServices, HotTours, OurStaff, BookTourNow, Gallery,
                     Contacts, Swiper, HeaderFooter)

# Register your models here.
admin.site.register(CreateYourTourStyle)
admin.site.register(BookTourNow)
admin.site.register(OurServices)
admin.site.register(HotTours)
admin.site.register(OurStaff)
admin.site.register(Gallery)
admin.site.register(Contacts)
admin.site.register(Swiper)
admin.site.register(HeaderFooter)




@admin.register(DiscoverNewHorizon)
class DiscoverNewHorizonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'buttonname')
    list_editable = ('name', 'description', 'buttonname')
    list_filter = ('buttonname',)
    search_fields = ('name',)


