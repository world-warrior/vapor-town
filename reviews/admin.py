from django.contrib import admin
from .models import ProductReviews

# Register your models here.
@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    baseModel = ProductReviews
    list_display = (
        'product',
        'user',
        'title',
        'content',
        'rating',
        'date',
        'times_updated',
        'previous_rating',
    )

    ordering = ('-date',)
