import os
import sys
from decimal import Decimal
from pathlib import Path

import django
from django.utils import timezone

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookhub.settings")
django.setup()

from main.models import Book, Listing, Store


def seed():
    store, _ = Store.objects.get_or_create(
        name="Jump Books",
        defaults={
            "website": "https://jumpbooks.lk/",
            "logo": "",
            "active_status": True,
        },
    )

    sample_books = [
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "isbn": "9781847941831",
            "category": "Self-Help",
            "language": "English",
            "publisher": "Arrow",
            "price": Decimal("4950.00"),
            "stock_status": "in_stock",
            "product_url": "https://jumpbooks.lk/atomic-habits",
            "discount_text": "10% Off",
        },
        {
            "title": "The Psychology of Money",
            "author": "Morgan Housel",
            "isbn": "9780857197689",
            "category": "Finance",
            "language": "English",
            "publisher": "Harriman House",
            "price": Decimal("5200.00"),
            "stock_status": "limited",
            "product_url": "https://jumpbooks.lk/psychology-of-money",
            "discount_text": "",
        },
        {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling",
            "isbn": "9780747532699",
            "category": "Fantasy",
            "language": "English",
            "publisher": "Bloomsbury",
            "price": Decimal("6100.00"),
            "stock_status": "in_stock",
            "product_url": "https://jumpbooks.lk/harry-potter-1",
            "discount_text": "",
        },
        {
            "title": "Thinking, Fast and Slow",
            "author": "Daniel Kahneman",
            "isbn": "9780141033570",
            "category": "Psychology",
            "language": "English",
            "publisher": "Penguin",
            "price": Decimal("5700.00"),
            "stock_status": "out_of_stock",
            "product_url": "https://jumpbooks.lk/thinking-fast-slow",
            "discount_text": "Voucher",
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "isbn": "9780061122415",
            "category": "Fiction",
            "language": "English",
            "publisher": "HarperOne",
            "price": Decimal("3800.00"),
            "stock_status": "in_stock",
            "product_url": "https://jumpbooks.lk/the-alchemist",
            "discount_text": "",
        },
    ]

    for entry in sample_books:
        book, _ = Book.objects.get_or_create(
            title=entry["title"],
            author=entry["author"],
            defaults={
                "isbn": entry["isbn"],
                "category": entry["category"],
                "language": entry["language"],
                "publisher": entry["publisher"],
            },
        )
        Listing.objects.update_or_create(
            book=book,
            store=store,
            defaults={
                "product_url": entry["product_url"],
                "price": entry["price"],
                "stock_status": entry["stock_status"],
                "discount_text": entry["discount_text"],
                "delivery_info": "",
                "last_updated": timezone.now(),
            },
        )


if __name__ == "__main__":
    seed()
    print("Seeded Jump Books data.")
