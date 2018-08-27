from django.shortcuts import render
from .models import Gists
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect


def gist_create_view(self):
    if self.method == 'GET':
        return render(self, 'gist_new.html')
    elif self.method == 'POST':
        data = self.POST
        gist = Gists()
        gist.code = self.POST.get('code')
        gist.language = self.POST.get('language')
        gist.user = self.user
        gist.expiration = self.POST.get('expiration')
        try:
            k=self.POST.get('sharable')
            gist.sharable = True
        except AttributeError:
            gist.sharable = False
        gist.save()
        return HttpResponseRedirect(reverse('gist_detail', args=[str(gist.id)]))


def gist_list_view(self):
    usr = self.user
    gists = Gists.objects.filter(user=usr)
    return render(self, 'gist_list.html', {'object_list': gists})


def gist_detail_view(self, pk):
    gist = Gists.objects.get(pk=pk)
    if (gist.user == self.user) | (gist.sharable is True):
        return render(self, 'gist_detail.html', {'object': gist})
    else:
        return HttpResponse('Unauthorized', status=401)


class GistUpdateView(UpdateView):
    model = Gists
    fields = ['code', 'sharable', 'language']
    template_name = 'gist_edit.html'


class GistDeleteView(DeleteView):
    model = Gists
    template_name = 'gist_delete.html'
    success_url = reverse_lazy('home')
