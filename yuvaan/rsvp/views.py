import pdb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import models
# Create your views here.


@login_required(login_url='/admin/')
def rsvp(request):
    rsvp_data = models.get_all_rsvp()
    rsvp_totals = models.get_all_rsvp_status()
    return render(request, 'rsvp.html', {'rsvp': rsvp_data,
                                         'rsvp_totals': rsvp_totals})


@login_required(login_url='/admin/')
def invitations(request):
    invitation_data = models.get_all_invitations()
    return render(request, 'invitation.html', {'invitations': invitation_data})
