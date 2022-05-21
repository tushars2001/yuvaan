import pdb

from django.shortcuts import render
from . import models
# Create your views here.


def rsvp(request):
    rsvp_data = models.get_all_rsvp()
    return render(request, 'rsvp.html', {'rsvp': rsvp_data})


def invitations(request):
    invitation_data = models.get_all_invitations()
    return render(request, 'invitation.html', {'invitations': invitation_data})
