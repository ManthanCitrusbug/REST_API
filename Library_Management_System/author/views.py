from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView
from .forms import AddAuthorForm
from library_admin.models import Book
from .models import Author
# Create your views here.

class AddAuthorView(CreateView):
    model = Author
    form_class = AddAuthorForm
    template_name = 'author/add_author.html'
    success_url = reverse_lazy('author:author-list')
    context = {}

    def get_template_names(self):
        return 'author/add_author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(deleted=False)
        return context


class AuthorListView(ListView):
    paginate_by = 10
    context_object_name = 'authors'
    model = Author
    template_name = 'author/author_list.html'
    queryset = Author.objects.filter(deleted=False).order_by('id')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_details.html'


class EditAuthorView(UpdateView):
    model = Author
    form_class = AddAuthorForm
    template_name = 'author/add_author.html'
    success_url = reverse_lazy('author:author-list')


class DeleteAuthorView(View):
    def get(self, request, pk):
        author = Author.objects.get(id=pk)
        if author.deleted == False:
            return render(request, 'author/delete_author.html')
        return redirect('author:author-list')
    
    def post(self, request, pk):
        author = Author.objects.get(id=pk)
        author.deleted = True
        author.save()
        return redirect('author:author-list')