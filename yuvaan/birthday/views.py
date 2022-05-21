import pdb

from django.shortcuts import render, redirect
from . import models
from ..rsvp.models import get_rsvp_by_guest_id


# Create your views here.


def first(request):
    guest_id = None
    guest_detail = {}
    rsvp_msg = None
    rsvp_details = None
    if request.method == 'GET' and 'guest' in request.GET and len(request.GET['guest']):
        guest_id = request.GET['guest']
        guest_detail = models.get_guest_by_id(guest_id)
        rsvp_details = get_rsvp_by_guest_id(guest_id)
    if request.method == 'POST' and 'guest' in request.POST and 'adults' in request.POST and 'kids' in request.POST \
            and 'status' in request.POST:
        register = models.register_rsvp(request.POST)
        guest_detail = models.get_guest_by_id(request.POST['guest'])
        rsvp_details = get_rsvp_by_guest_id(request.POST['guest'])
        rsvp_msg = 'Thanks ' + guest_detail['invitee'] + '! Your RSVP is registered.'
        return redirect("/turning-1/?guest=" + request.POST['guest'])
    return render(request, "first.html",
                  {'guest_detail': guest_detail, 'rsvp_msg': rsvp_msg, 'rsvp_details': rsvp_details})
