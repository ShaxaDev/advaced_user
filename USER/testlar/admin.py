from django.contrib import admin

from testlar.models import Book

from testlar.models import Review


class ReviewInline(admin.TabularInline):
    model=Review

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
admin.site.register(Book,BookAdmin)