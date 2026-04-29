from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404, render

from .models import Book, Listing


def search(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.all()
    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(isbn__icontains=query)
        )

    listings_query = Listing.objects.select_related("store").order_by("price")
    books = books.prefetch_related(Prefetch("listings", queryset=listings_query))

    results = []
    for book in books:
        listings = list(book.listings.all())
        lowest_listing = listings[0] if listings else None
        results.append(
            {
                "book": book,
                "listings": listings,
                "lowest_listing": lowest_listing,
            }
        )

    context = {
        "query": query,
        "results": results,
    }
    return render(request, "main/search.html", context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    listings = book.listings.select_related("store").order_by("price")
    context = {
        "book": book,
        "listings": listings,
        "lowest_listing": listings[0] if listings else None,
    }
    return render(request, "main/book_detail.html", context)