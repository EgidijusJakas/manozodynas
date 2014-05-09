from django.shortcuts import render

from .models import Word
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def words_view(request):
    return render(request, 'manozodynas/words.html', {'words': Word.objects.all()})

class NewWord(CreateView):
    model = Word
    success_url = reverse_lazy('words')
    template_name = 'manozodynas/new_word.html'

