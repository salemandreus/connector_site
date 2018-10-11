from django.contrib import admin
from meetups_list.models import MeetupCategory, Meetup, BookingSpaces, Organiser

admin.site.register(MeetupCategory)
#admin.site.register(Meetup)
#admin.site.register(BookingSpaces)
#admin.site.register(Organiser)

@admin.register(Organiser)
class OrganiserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    fields = ['first_name', 'last_name', ('date_of_birth')]

class BookingSpaceInline(admin.TabularInline):
    model = BookingSpaces

@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('name', 'organiser', 'display_meetup_category')
    inlines = [BookingSpaceInline]


@admin.register(BookingSpaces) 
class BookingSpacesAdmin(admin.ModelAdmin):
    list_filter = ('status', 'date')
    fieldsets = (
        (None, {
            'fields': ('meetup', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'date')
        }),
    )
