import pdb

from django.shortcuts import render
from . import models
# Create your views here.


def rsvp(request):
    rsvp_data = models.get_all_rsvp()
    rsvp_totals = models.get_all_rsvp_status()
    return render(request, 'rsvp.html', {'rsvp': rsvp_data,
                                         'rsvp_totals': rsvp_totals})


def invitations(request):
    invitation_data = models.get_all_invitations()
    return render(request, 'invitation.html', {'invitations': invitation_data})
