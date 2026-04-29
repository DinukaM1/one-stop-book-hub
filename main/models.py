from django.db import models
from django.utils.text import slugify


class Book(models.Model):
	title = models.CharField(max_length=255, db_index=True)
	author = models.CharField(max_length=255, blank=True, db_index=True)
	isbn = models.CharField(max_length=32, blank=True, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)
	description = models.TextField(blank=True)
	image_url = models.URLField(blank=True)
	category = models.CharField(max_length=100, blank=True)
	language = models.CharField(max_length=50, blank=True)
	publisher = models.CharField(max_length=120, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(self.title)[:240] or "book"
			slug = base_slug
			counter = 2
			while Book.objects.filter(slug=slug).exclude(pk=self.pk).exists():
				slug = f"{base_slug}-{counter}"
				counter += 1
			self.slug = slug
		super().save(*args, **kwargs)

	def __str__(self):
		if self.author:
			return f"{self.title} - {self.author}"
		return self.title


class Store(models.Model):
	name = models.CharField(max_length=120, unique=True)
	website = models.URLField()
	logo = models.URLField(blank=True)
	active_status = models.BooleanField(default=True)

	def __str__(self):
		return self.name


class Listing(models.Model):
	STOCK_STATUS_CHOICES = [
		("in_stock", "In Stock"),
		("out_of_stock", "Out of Stock"),
		("limited", "Limited"),
	]

	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="listings")
	store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="listings")
	product_url = models.URLField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock_status = models.CharField(
		max_length=20, choices=STOCK_STATUS_CHOICES, default="in_stock"
	)
	discount_text = models.CharField(max_length=100, blank=True)
	delivery_info = models.CharField(max_length=150, blank=True)
	last_updated = models.DateTimeField(auto_now=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=["book", "store"], name="unique_book_store_listing"
			)
		]

	def __str__(self):
		return f"{self.book.title} @ {self.store.name}"
