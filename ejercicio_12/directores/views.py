from django.views import generic

from .models import Director, Pelicula

class IndexView(generic.ListView):
    template_name = 'directores.html'
    model = Director

class DirectorView(generic.DetailView):
    template_name = 'director.html'
    model = Director

class PeliculaView(generic.DetailView):
    template_name = 'pelicula.html'
    model = Pelicula