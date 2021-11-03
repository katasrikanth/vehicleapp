from django.db.models.fields import SlugField
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Vehicle
# Create your views here.

class listofvehicle(ListView):
    model = Vehicle
    template_name = 'vapp/vehicle_list.html'

class createvehicle(CreateView):
    model = Vehicle
    template_name = 'vapp/vehicle_new.html'
    fields = ['vehiclename','speed','avgspeed','Temperature','fuellevel','enginestats','image1','image2']
    success_url = reverse_lazy('home')


class detailvehicle(DetailView):
    model = Vehicle
    template_name = 'vapp/vehicle_detail.html'
    

class updatevehicle(UpdateView):
    model = Vehicle
    template_name = 'vapp/vehicle_update.html'    
    fields = ['vehiclename','speed','avgspeed','Temperature','fuellevel','enginestats','image1','image2']

class deletevehicle(DeleteView):
    model = Vehicle
    template_name = 'vapp/vehicle_delete.html'
    success_url = reverse_lazy('home')

