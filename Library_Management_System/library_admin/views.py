from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from library_admin.forms import AddBookForm, AdminLoginForm, AdminRegisterform, Issue_Book_Form, Issue_Book_Edit_Form, EditBookForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth import authenticate, login, logout
from library_admin.models import Book, Issued_Book

# Create your views here.

class IntexView(TemplateView):
    template_name = 'index.html'


class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterform
    template_name = 'admin_register.html'
    success_url = 'admin-login'


class AdminLoginView(View):
    def post(self,request):
        form = AdminLoginForm(request.POST)
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user_name,password=password)
        if user is not None: 
            login(request, user)
            return redirect('library_admin:admin-dashboard')
        else:
            return render(request,'admin_login.html',{'form':form}) 

    def get(self,request):
        form = AdminLoginForm()
        return render(request,'admin_login.html',{'form':form})


class AdminDashboardView(ListView):
    paginate_by = 7
    model = Book
    context_object_name = 'books'
    template_name = 'admin_dashboard.html'
    queryset = Book.objects.filter(deleted=False).order_by('id')


class AdminLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('library_admin:index')


class AddBookView(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = 'book/add_book.html'
    success_url = 'admin-dashboard'


class EditBookView(UpdateView):
    model = Book
    form_class = EditBookForm
    template_name = 'book/add_book.html'
    success_url = reverse_lazy('library_admin:admin-dashboard')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class DeleteBookView(View):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        if book.deleted == False:
            return render(request, 'book/delete_book.html')
        return redirect('library_admin:admin-dashboard')

    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        book.deleted = True
        book.save()
        return redirect('library_admin:admin-dashboard')

    
class IssueBookView(CreateView):
    model = Issued_Book
    form_class = Issue_Book_Form
    template_name = 'book/issue_book.html'
    success_url = 'issued-books-list'


class IssuedBooksListView(ListView):
    paginate_by = 7
    model = Issued_Book
    context_object_name = 'books'
    template_name = 'book/issued_book_list.html'
    queryset = Issued_Book.objects.all().order_by('id')


class IssuedBookDetailsView(DetailView):
    model = Issued_Book
    template_name = 'book/issued_details.html'


class IssuedBookEditView(UpdateView):
    model = Issued_Book
    form_class = Issue_Book_Edit_Form
    template_name = 'book/edit_issued_book.html'
    success_url = reverse_lazy('library_admin:issued-books-list')


class IssuedBookDeleteView(DeleteView):
    model = Issued_Book
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('library_admin:issued-books-list')