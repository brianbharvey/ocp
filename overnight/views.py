from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Guest, Intake, Turnaway
from .forms import GuestForm, IntakeForm, TurnawayForm
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def new_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'guest_form.html', {'form': form})

def update_guest(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'guest_form.html', {'form': form})

def guest_list(request):
    guests = Guest.objects.all()
    paginator = Paginator(guests, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'guest_list.html', {'page_obj': page_obj})

def new_intake(request):
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('intake_list')
    else:
        form = IntakeForm(initial={'date': timezone.now().date()})
    return render(request, 'intake_form.html', {'form': form})

def update_intake(request, pk):
    intake = get_object_or_404(Intake, pk=pk)
    if request.method == 'POST':
        form = IntakeForm(request.POST, instance=intake)
        if form.is_valid():
            form.save()
            return redirect('intake_list')
    else:
        form = IntakeForm(instance=intake)
    return render(request, 'intake_form.html', {'form': form})

def intake_list(request):
    intakes = Intake.objects.all()
    return render(request, 'intake_list.html', {'intakes': intakes})

def new_turnaway(request):
    if request.method == 'POST':
        form = TurnawayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnaway_list')
    else:
        form = TurnawayForm(initial={'date': timezone.now().date()})
    return render(request, 'turnaway_form.html', {'form': form})

def update_turnaway(request, pk):
    turnaway = get_object_or_404(Turnaway, pk=pk)
    if request.method == 'POST':
        form = TurnawayForm(request.POST, instance=turnaway)
        if form.is_valid():
            form.save()
            return redirect('turnaway_list')
    else:
        form = TurnawayForm(instance=turnaway)
    return render(request, 'turnaway_form.html', {'form': form})

def turnaway_list(request):
    turnaways = Turnaway.objects.all()
    return render(request, 'turnaway_list.html', {'turnaways': turnaways})

# Add statistics view logic here as needed
def Statistics(request):
    return render(request, 'statistics.html')