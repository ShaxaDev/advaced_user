from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import UserC
from .models import Book


def sign(request):
    form=UserC()
    if request.method=='POST':
        form=UserC(request.POST)
        u=form.save(commit=False)
        u.set_password(form.cleaned_data['password'])
        u.save()
        return redirect('login')
    return render(request,'registration/register.html',{'form':form})


class BookList(ListView):
    model=Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'

class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


