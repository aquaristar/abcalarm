from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import AlarmForm
from .models import Alarm
from plyer import notification
from plyer.compat import PY2


# Create your views here.

def index(request):
    context = {
        'alarm_list': Alarm.objects.all(),
    }
    return render(request, "index.html", context)


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
