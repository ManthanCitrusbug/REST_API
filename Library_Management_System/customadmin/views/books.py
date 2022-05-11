from multiprocessing import context
from django.views import View
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyDetailView,
    MyLoginRequiredView,
    MyUpdateView,
)
from library_admin.forms import EditBookForm, AddBookForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView, DetailView
from django_datatables_too.mixins import DataTableMixin
from library_admin.forms import AdminRegisterform
from library_admin.models import Book
from author.models import Author
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
import csv

# Export CSV FILE

def export_user_csv(request):

    output = []
    response = HttpResponse (content_type='text/csv')
    filename = u"User.csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(filename)

    writer = csv.writer(response)
    query_set = User.objects.all()

    #Header
    writer.writerow(['Name', "Username",'Bio', 'Email', 'Status','Phone','User Type',"is_staff", "is_superuser","avatar","company"])
    for user in query_set:
        if user.groups.all():
            gp = user.groups.all()[0].name
        else:
            gp = None

        if not user.profile_image:
            avatar = None
        else:
            avatar = user.profile_image.url


        output.append([user.first_name, user.last_name, user.username, user.email, user.is_active,gp,user.is_staff, user.is_superuser, request.build_absolute_uri(avatar),])
    #CSV Data
    writer.writerows(output)
    return response


class BookDetailsView(MyDetailView):
    template_name = "customadmin/service/service_detail.html"
    context = {}

    def get(self, request, pk):
        self.context['service_detail'] = Book.objects.filter(pk=pk).first()
        return render(request, self.template_name, self.context)


class BookListView(MyListView):
    ordering = ["id"]
    model = Book
    queryset = Book.objects.all()
    template_name = "customadmin/service/service_list.html"
    permission_required = ("customadmin.view_book",)
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.all()
        return super().get_context_data(**kwargs)


class BookCreateView(MyCreateView):
    model = Book
    form_class = AddBookForm
    template_name = "customadmin/service/service_form.html"
    permission_required = ("customadmin.add_book",)


class BookDeleteView(MyDeleteView):
    model = Book
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customadmin.delete_book",)

    def get_success_url(self):
        return reverse("customadmin:book-list")


class BookUpdateView(MyUpdateView):
    model = Book
    form_class = EditBookForm
    template_name = "customadmin/service/update.html"

    def get_success_url(self):
        return reverse("customadmin:book-list")


class BookAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    model = Book
    queryset = Book.objects.all()

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        # ctx.update({"obj": obj})
        # print(ctx)
        return t.render({"o": obj})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
                # | Q(state__icontains=self.search)
                # | Q(year__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data

    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""


    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        # ctx.update({"obj": obj})
        # print(ctx)
        return t.render({"o": obj})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
                # | Q(state__icontains=self.search)
                # | Q(year__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data