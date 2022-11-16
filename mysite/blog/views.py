from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def home(request):
    context={}
    articles=Article.objects.all()
    paginatior=Paginator(articles,2)
    page_number=request.GET.get('page')
    page=paginatior.get_page(page_number)
    print('Page-',page)
    context['articles']=page
    return  render(request,'blog/index.html',context)
