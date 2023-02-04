from django.shortcuts import render
from .models import Content

# Create your views here.
def index(request):
  contents = Content.objects.order_by("-published_at")
  return render(request, "index.html", {"contents":contents})