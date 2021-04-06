from django.shortcuts import render, redirect
from .models import Projects, Votes, Comments, Profile
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    
    try:
        projects = Projects.objects.all()
    except Exception as e:
        raise Http404()
    return render(request, "index.html", {"projects": projects})