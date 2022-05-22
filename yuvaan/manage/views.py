import pdb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..rsvp.models import get_all_invitations
from django.utils.http import urlencode
from . import models
# Create your views here.


@login_required(login_url='/manage/login/')
def manage_home(request):
    return render(request, "manage_home.html")


def login(request):
    if request.method == 'POST' and 'passcode' in request.POST and request.POST['passcode'] == 'arjun@0331':
        return render(request, "manage_home.html")
    return render(request, "login.html")


def guests(request):
    guest_details = get_all_invitations()
    if request.method == 'POST' and 'action' in request.POST and request.POST['action'] == 'add':
        models.add_guest(request.POST)
        return redirect("/manage/guests/?message=" + request.POST['invitee'].replace("&", "-") + " Added.")
    if request.method == 'POST' and 'action' in request.POST and request.POST['action'] == 'update':
        models.update_guest(request.POST)
        return redirect("/manage/guests/?message=" + (request.POST['invitee']).replace("&", "-") + " updated.")
    return render(request, "manage_guests.html", {'guest_details': guest_details})


def rsvp_status(request):
    return redirect("/rsvp/")