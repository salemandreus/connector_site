from django.shortcuts import render

from meetups_list.models import Meetup, Organiser, BookingSpaces, MeetupCategory

def index(request):
    """View function for home page of site."""

    num_meetups = Meetup.objects.all().count()
    #num_spaces = BookingSpaces.objects.all().count()
    #num_spaces_available = BookingSpaces.objects.filter(status__exact='u').count()
    
    num_organisers = Organiser.objects.count()
    
    context = {
        'num_meetups': num_meetups,
        #'num_spaces': num_spaces,
        #'num_spaces_available': num_spaces_available,
        'num_organisers': num_organisers,
    }

    return render(request, 'index.html', context=context)
