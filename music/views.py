from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView
from .forms import DocumentForm
from .models import Document
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .music_genre import genre
from .mel_spectogram import mel_spec
import numpy as np

import warnings
warnings.simplefilter('ignore')

# Create your views here.
class IndexView(ListView):
    template_name= 'music/index.html'
    def get_queryset(self):
        return True

# class GenreView(TemplateView):
#     form_class= DocumentForm
#     template_name = 'music/check_genre.html'

def model_form_upload(request):
    documents = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            newdoc = Document(file=request.FILES['file'])
            newdoc.save()
            print(newdoc.file.name)
            result = genre(newdoc)
            label = result.argmax()
            a = np.array(result).tolist()
            b = a[0]
            x=b[0]*100
            y=b[1]*100
            z=b[2]*100
            context ={'documents':documents,'form':form,'result':result,'x':x,'y':y,'z':z,'label':label}
            return render(request,'music/result.html',context)
    else:
        form = DocumentForm()

    return render(request,'music/result.html',{'documents':documents,'form':form})
