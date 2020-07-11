# from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class SchoolListView(generic.ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(generic.DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(generic.CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(generic.UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(generic.DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
