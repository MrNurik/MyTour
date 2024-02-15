
from .models import New_bookings
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages


def base(request):
    return render(request, 'index.html')


def booking(request):
    bookings = New_bookings.objects.all()
    return render(request, 'booking.html', {'bookings': bookings})


def register(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            messages.error(request, "Бұл уақыт брондалған. Басқа күнді таңдаңыз.")
    else:
        form = BookingForm()
    return render(request, 'register.html', {'form': form})


def readmore(request):
    return render(request, 'readmore.html')
