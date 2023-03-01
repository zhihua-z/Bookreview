from django.http import Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_book_list = ['斗罗大陆', '斗破苍穹']

    context = {
        'latest_book_list': latest_book_list,
    }
    
    return render(request, 'booklist/index.html', context)