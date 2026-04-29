from django.contrib import admin

from .models import Book, Listing, Store


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "isbn", "category", "language")
	search_fields = ("title", "author", "isbn")
	prepopulated_fields = {"slug": ("title",)}


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ("name", "website", "active_status")
	list_filter = ("active_status",)
	search_fields = ("name",)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
	list_display = ("book", "store", "price", "stock_status", "last_updated")
	list_filter = ("stock_status", "store")
	search_fields = ("book__title", "store__name")
