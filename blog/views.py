from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Menu, BookATable


class IndexTemplateView(TemplateView):
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        response= super().get(request, *args, **kwargs)
        return response

class MenuListView(ListView):
    template_name = 'blog/menu.html'
    context_object_name = 'menu'
    model = Menu

    def get_queryset(self):
        from itertools import zip_longest
        objs = Menu.objects.filter(is_published=True)
        objs = iter(objs)
        return list(zip_longest(objs, objs))

def home(request):
    return render(request, 'blog/index.html')

class AboutTemplateView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        a = 5
        context['heading'] = ('О нас {a}').format(a=a)
        context['subheading'] = ('Наша еда')
        return context

class BookATable(ListView):
    template_name = 'blog/book.html'
    context_object_name = 'book'
    model = BookATable