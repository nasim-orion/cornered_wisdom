from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote

def home(request):

    quotes = Quote.objects.filter(user=request.user)

    quote = None

    if request.GET.get("shuffle"):
        quote = quotes.order_by("?").first()
    else:
        quote = quotes.order_by("?").first()

    return render(request, "home/home.html", {
        "quotes": quotes,
        "quote": quote,
    })
