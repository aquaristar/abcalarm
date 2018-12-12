from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import AlarmForm
from .models import Alarm


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
            form = AlarmForm(request.POST)
            if form.is_valid():
                form.save()
                result = "ok"
            else:
                result = "api parameters are not valid."
        else:
            result = "api method is POST type."
    except:
        result = "failed"
    return HttpResponse(result)
