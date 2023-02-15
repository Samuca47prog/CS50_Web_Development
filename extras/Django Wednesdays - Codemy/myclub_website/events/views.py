from django.shortcuts import render

import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .models import Event

def all_events(request):
    event_list = Event.objects.all()

    return render(request, 'events/events_list.html', {
        'event_list': event_list
    })

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    month = month.capitalize()
    month_number = datetime.strptime(month, '%B').month
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )

    return render(request, 'events\home.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal
    })
