import pdb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..rsvp.models import get_all_invitations
from django.utils.http import urlencode
from . import models
# Create your views here.


@login_required(login_url='/admin/', redirect_field_name='next')
def manage_home(request):
    return render(request, "manage_home.html")


def login(request):
    if request.method == 'POST' and 'passcode' in request.POST and request.POST['passcode'] == 'arjun@0331':
        return render(request, "manage_home.html")
    return render(request, "login.html")


@login_required(login_url='/admin/')
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


@login_required(login_url='/admin/')
def messages(request):
    message_data = models.get_all_messages()
    return render(request, "messages.html", {'message_data': message_data})
