from django.contrib import admin
from library_admin.models import Book, Category, Issued_Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'category']


@admin.register(Issued_Book)
class Issued_Book_Admin(admin.ModelAdmin):
    list_display = ['username', 'book', 'email', 'issued_date', 'return_date', 'total_charge']


admin.site.register(Category)
