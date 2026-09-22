from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote


def home(request):
    quotes = Quote.objects.filter(user=request.user)
    return render(request, "home/home.html", {
        "quotes": quotes
    })