from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.db.models import  Q



from .models import Event
from .forms import EventForm

#Base_HLS_URL = 'http://live.balajidigitals.in:8080/live/'
#Base_RTMP_URL = 'rtmp://stream.balajidigitals.in/live/'
Base_INTENT = "intent://stream.balajidigitals.in/live/"

Base_HLS_URL = 'http://localhost:8080/live/'
Base_RTMP_URL = 'rtmp://127.0.0.1/live/'
# Create your views here.
@login_required
def Index(request):
    events = Event.objects.filter(~Q(status='COMPLETED'))
    return render(request, 'index.html',{'events': events})

def Event_Stream(request, id):
    event= get_object_or_404(Event, pk=id)
    current_time = timezone.localtime(timezone.now())
    if event.end_date_time <= current_time:
        ext = '.mp4'
    else:
        ext = '.m3u8'
    hlsurl = Base_HLS_URL +event.Stream_Key + '/' +event.Stream_Key + ext
    rtmpurl = Base_RTMP_URL + event.Stream_Key
    intenturl = Base_INTENT + event.Stream_Key + '/' +event.Stream_Key + ext
    if event.start_date_time <= current_time :
        return render(request, 'event.html', {'event': event, 'hlsurl': hlsurl , 'rtmpurl': rtmpurl, 'intenturl' : intenturl})
    else:
        return HttpResponse("<h1>Invalid Stream</h1>")

@login_required
#@user_passes_test(Permission_Check,redirect_field_name= None)
def Event_Add(request):
    files = request.FILES
    for f in files:
        print("printing file : ")
        print(f)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect(reverse('livestream:index'))
    else:
        form = EventForm()
    return render(request, 'live_event_add.html',{'form':form})
