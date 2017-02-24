# encoding: utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from noticias.models import Noticias
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
# Create your views here.
from django.template import RequestContext
from noticias.form import NoticiasForm
from django.utils import timezone

def noticias(request):
    noticias = Noticias.objects.order_by('-fecha_publicacion')
    return render(request, 'noticias.html',{'noticias':noticias})   
    #return render_to_response('noticias.html',{'noticias':noticias})


#@csrf_exempt
def crearNoticia(request):
    
    if request.method == 'POST':
        form_noticia=NoticiasForm(request.POST)
        if form_noticia.is_valid():
           form_noticia.save()
        return HttpResponseRedirect('noticias')
    else:
    	form_noticia=NoticiasForm()
    return render(request, 'noticia_crear.html', {'form_noticia':form_noticia})
