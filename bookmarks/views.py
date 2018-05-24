from django.shortcuts import render
from .models import Bookmark

# Create your views here.
def index(request):
  context = {
    'bookmarks': Bookmark.objects.all(), #pylint: disable=E1101
  }

  return render(request, 'bookmarks/index.html', context)
