from django.db import models

class MeetupCategory(models.Model):
    """Model representing a meetup category."""
    name = models.CharField(max_length=200, help_text='Enter a meetup category (e.g. Javascript meetup)')
    
    def __str__(self):
        return self.name

from django.urls import reverse

class Meetup(models.Model):
    name = models.CharField(max_length=200)
    organiser = models.ForeignKey('Organiser', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text='Enter a description of the meetup')    
    meetupCategory = models.ManyToManyField(MeetupCategory, help_text='Select a MeetupCategory for this Meetup')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('meetup-detail', args=[str(self.id)])

    def display_meetup_category(self):
        return ', '.join(meetupCategory.name for meetupCategory in self.meetupCategory.all()[:3]) 
    display_meetup_category.short_description = 'MeetupCategory'

import uuid 

class BookingSpaces(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular booking space')
    meetup = models.ForeignKey('Meetup', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)

    ACTIVE_STATUS = (		        
       ('c', 'Cancelled'),			        
       ('p', 'Passed'),
       ('u', 'Upcoming'),
       ('i', 'In Progress'),
    )

    status = models.CharField(
        max_length=1,
        choices=ACTIVE_STATUS,
        blank=True,
        default='u',
        help_text='meetup availability'
    )

    class Meta:
        ordering = ['date']

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id,self.meetup.name)

class Organiser(models.Model):
    """Model representing an organiser."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        return reverse('organiser-detail', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.last_name,self.first_name)
