from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import UpdateView
from .forms import ProductReviewForm
from products.models import AllProducts
from django.contrib import messages
from .models import ProductReviews

# Create your views here.


class CreateReview(View):
    """"
    View to create a review from the product details page
    """

    def get(self, request, product_id):
        product = get_object_or_404(AllProducts, id=product_id)
        form = ProductReviewForm()
        context = {
            'review_form': form,
            'product': product,
        }
        return render(request, 'reviews/review-form-page.html', context)

    def post(self, request, product_id):
        product = get_object_or_404(AllProducts, id=product_id)
        redirect_url = request.POST.get('redirect_url')
        if redirect_url != f'/products/{product_id}/':
            redirect_url = f'/products/{product_id}/'
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            messages.success(request, 'Review successfully added!')
            return redirect(redirect_url)
        else:

            messages.error(request, 'Failed to add review. Please ensure \
                the form title is valid and you have entered a rating \
                    as a whole number between 1 and 5 (no decimals).')

            return redirect('add_review', product_id)


# class EditReview(UpdateView):
#     """"
#     View to edit a review from the product details page
#     """
#     model = ProductReviews
#     template_name = 'reviews/review-form-page.html'
#     form_class = ProductReviewForm
#     success_url = '/products/{review_product_id}/'

    # def get(self, request, review_id):
    #     review = get_object_or_404(ProductReviews, id=review_id)
    #     product = review.product
    #     form = ProductReviewForm(instance=review)
    #     context = {
    #         'review_form': form,
    #         'review': review,
    #         'product': product,
    #     }
    #     return render(request, 'reviews/review-form-page.html', context)

    # def post(self, request, review_id):
    #     review = get_object_or_404(ProductReviews, id=review_id)
    #     redirect_url = request.POST.get('redirect_url')
    #     if redirect_url != f'/products/{review.product.id}/':
    #         redirect_url = f'/products/{review.product.id}/'
    #     form = ProductReviewForm(instance=review)
    #     if form.is_valid():
            
    #         review.save()
    #         messages.success(request, 'Review successfully updated!')
    #         return redirect(redirect_url)
    #     else:
    #         messages.error(request, 'Failed to update review. Please ensure \
    #             the form title is valid and you have entered a rating \
    #                 as a whole number between 1 and 5 (no decimals).')
    #         return redirect('edit_review', review_id)

