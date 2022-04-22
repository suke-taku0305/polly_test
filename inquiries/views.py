from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import forms

# Create your views here.
class IndexView(generic.FormView):
    template_name = "inquiries/index.html"
    form_class = forms.InquiryForm
    success_url = reverse_lazy('inquiries:index')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)