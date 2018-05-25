from django.shortcuts import render
from .models import Bookmark, PersonalBookmark

# Create your views here.
#pylint: disable=E1101
def index(request):
  context = {}

  pbid = PersonalBookmark.objects.values_list('id')

  context['bookmarks'] = Bookmark.objects.exclude(id__in=pbid)

  # context = {
  #   'bookmarks': Bookmark.objects.exclude(id_in=pbid),
  #   'personal_bookmarks': PersonalBookmark.objects.filter(user=request.user),
  # }

  if request.user.is_anonymous:
    context['personal_bookmarks'] = PersonalBookmark.objects.none()
  else:
      context['personal_bookmarks'] = PersonalBookmark.objects.filter(user=request.user)

  return render(request, 'bookmarks/index.html', context)
