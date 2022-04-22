from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from boto3 import Session
from contextlib import closing
from .models import Polly
from django.conf import settings
from django.core.files.base import ContentFile

# Create your views here.
class PollyListView(generic.ListView):
  model = Polly
  template_name = 'polly/list.html'

class PollyDetailView(generic.DetailView):
  model = Polly
  template_name = 'polly/detail.html'

class PollyCreateView(generic.CreateView):
    model = Polly
    template_name = 'polly/create.html'
    success_url = reverse_lazy('polly:list')
    fields = ['talker','remark']

    def form_valid(self, form):
        polly = form.save(commit=False)
        response = use_polly(polly.talker, polly.remark)
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as streamingbody:
                data = streamingbody.read()
                polly.audio.save(str(polly.id)+'.mp3',ContentFile(data))
        polly.save()
        return super().form_valid(form)

def use_polly(voice,remark):
        
    #create session
    session = Session(profile_name="default")
    polly = session.client("polly")

    response = polly.synthesize_speech(
        Text = remark,
        OutputFormat = "mp3",
        VoiceId = voice
    )

    return response
