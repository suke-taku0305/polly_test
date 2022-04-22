from django.shortcuts import render
from django.views import generic
from .models import Skill
from django.urls import reverse_lazy

# Create your views here.
class SkillCreateView(generic.CreateView):
    model = Skill
    template_name = 'skills/create.html'

    fields = '__all__'
    success_url = reverse_lazy('skills:list')

class SkillListView(generic.ListView):
    model = Skill
    template_name = 'skills/list.html'

    def get_queryset(self):
        return Skill.objects.all().order_by('name')

class SkillDetailView(generic.DetailView):
    model = Skill
    template_name = 'skills/detail.html'

class SkillUpdateView(generic.UpdateView):
    model = Skill
    template_name = 'skills/update.html'

    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('skills:detail', kwargs={'pk':self.kwargs['pk']})

class SkillDeleteView(generic.DeleteView):
    model = Skill
    template_name = 'skills/delete.html'
    success_url = reverse_lazy('skills:list')