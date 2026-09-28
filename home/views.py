from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Quote, Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Case, When, Value, IntegerField

@login_required
def home(request):

    quotes = Quote.objects.filter(user=request.user)
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


@login_required
def add_quote(request):
    if request.method == "POST":
        page_number = request.POST["page_number"]

        if page_number and int(page_number) < 1:
            return render(request, "home/add_quote.html", {
                "error": "Page number must be 1 or above."
            })

        book = Book.objects.create(
            title=request.POST["book_title"],
            author=request.POST["author"]
        )

        Quote.objects.create(
            user=request.user,
            book=book,
            text=request.POST["text"],
            page_number=int(page_number) if page_number else None,
            notes=request.POST["notes"]
        )

        return redirect("home")

    return render(request, "home/add_quote.html")




@login_required
def my_quotes(request):
    quotes = Quote.objects.filter(user=request.user)
    
    sort = request.GET.get("sort", "newest")

    if sort == "oldest":
           quotes = quotes.order_by("created_at")

    elif sort == "book":
           quotes = quotes.order_by("book__title")

    elif sort == "author":
     quotes = quotes.annotate(
        author_blank=Case(
            When(book__author="", then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        )
    ).order_by("author_blank", "book__author")

    else:
           quotes = quotes.order_by("-created_at")


    return render(request, "home/my_quotes.html", {
        "quotes": quotes,
        "sort": sort
    })


@login_required
def shuffle_quote(request):
    quotes = Quote.objects.filter(user=request.user)

    current_quote_id = request.GET.get("current")

    if current_quote_id and quotes.count() > 1:
     quotes = quotes.exclude(id=current_quote_id)

    quote = quotes.order_by("?").first()

    if quote:
        return render(request, "home/quote_partial.html", {
            "quote": quote
        })

    return render(request, "home/quote_partial.html", {
        "quote": None
    })




@login_required
def edit_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id, user=request.user)

    if request.method == "POST":
        page_number = request.POST["page_number"]

# Prevents page numbers less than 1 from being saved to the database.

        if page_number and int(page_number) < 1:
            return render(request, "home/edit_quote.html", {
                "quote": quote,
                "error": "Page number must be 1 or above."
            })

        quote.text = request.POST["text"]
        quote.book.title = request.POST["book_title"]
        quote.book.author = request.POST["author"]
        quote.page_number = int(page_number) if page_number else None
        quote.notes = request.POST["notes"]

        quote.book.save()
        quote.save()

        return redirect("my_quotes")

    return render(request, "home/edit_quote.html", {
        "quote": quote
    })

@login_required
def delete_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id, user=request.user)

    if request.method == "POST":
        quote.delete()
        return redirect("my_quotes")

    return render(request, "home/delete_quote.html", {
        "quote": quote
    })


def about(request):
    return render(request, "home/landing.html")

def about(request):
    return render(request, "home/landing.html")