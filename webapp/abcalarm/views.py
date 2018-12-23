from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import AlarmForm
from .models import Alarm, ALARM_STATUS, ALARM_TYPE
from plyer import notification
from plyer.compat import PY2
from datetime import datetime, timedelta, time
from django.utils import timezone


# Create your views here.

def index(request):
    time_threshold = datetime.now().date() - timedelta(hours=5)
    #today_start = datetime.combine(datetime.now().date(), time())
    today_start = timezone.localtime(timezone.now()).date()
    yesterday_start = timezone.localtime(timezone.now()).date() - timedelta(1)
    print(today_start)
    context = {
        'alarm_list': Alarm.objects.all().order_by('-created_date'),
        'total': len(Alarm.objects.all()),
        'new': len(Alarm.objects.filter(status='new')),
        'checked': len(Alarm.objects.filter(status='checked')),
        'today': len(Alarm.objects.filter(created_date__gte=today_start)),
        'yesterday': len(Alarm.objects.filter(created_date__gte=yesterday_start, created_date__lt=today_start)),
    }
    return render(request, "index.html", context)

def checked_alarm(request, pk):
    if request.method == "GET":
        alarm = Alarm.objects.get(pk=pk)
        alarm.status = 'checked'
        alarm.save()
    return redirect('/abcalarm/')

@csrf_exempt
def alarm(request):
    try:
        if request.method == "POST":
            new_alarm = Alarm()
            form = AlarmForm(request.POST, instance=new_alarm)
            if form.is_valid():
                kwargs = {
                    'app_name': 'ABC Warehouse',
                    'title': new_alarm.title,
                    'message': new_alarm.message,
                    'ticker': 'r',
                    'app_icon': './static/ico/plyer-icon.ico',
                    'timeout': 10,
                }
                notification.notify(**kwargs)
                form.save()
                result = "ok"
            else:
                result = "api parameters are not valid."
        else:
            result = "api method is POST type."
    except:
        result = "failed"
    return HttpResponse(result)
