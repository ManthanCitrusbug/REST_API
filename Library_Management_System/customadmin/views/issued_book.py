from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyDetailView,
    MyLoginRequiredView,
    MyUpdateView,
)
from library_admin.forms import Issue_Book_Form, Issue_Book_Edit_Form
from library_admin.models import Issued_Book
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin
from django.shortcuts import render
from django.urls import reverse

class IssuedBookDetailsView(MyDetailView):
    template_name = "customadmin/issued_book/issued_book_detail.html"
    context = {}

    def get(self, request, pk):
        self.context['issued_dook'] = Issued_Book.objects.filter(pk=pk).first()
        return render(request, self.template_name, self.context)


class IssuedBookListView(MyListView):
    ordering = ["-id"]
    model = Issued_Book
    queryset = Issued_Book.objects.all()
    template_name = "customadmin/issued_book/issued_book_list.html"
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issued_dook'] = Issued_Book.objects.all()
        return super().get_context_data(**kwargs)


class IssuedBookCreateView(MyCreateView):
    model = Issued_Book
    form_class = Issue_Book_Form
    template_name = "customadmin/issued_book/issued_book_form.html"

    def get_success_url(self):
        return reverse("customadmin:issued_book-list")


class IssuedBookDeleteView(MyDeleteView):
    model = Issued_Book
    template_name = "customadmin/confirm_delete.html"

    def get_success_url(self):
        return reverse("customadmin:issued_book-list")


class IssuedBookUpdateView(MyUpdateView):
    model = Issued_Book
    form_class = Issue_Book_Edit_Form
    template_name = "customadmin/issued_book/issued_book_update.html"

    def get_success_url(self):
        return reverse("customadmin:issued_book-list")


class IssuedBookAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    model = Issued_Book
    queryset = Issued_Book.objects.all()

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