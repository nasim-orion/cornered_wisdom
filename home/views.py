from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
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


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        "form": form
    })