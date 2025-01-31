from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.

# View for the categories
def categories(request):

    return {
        'categories': Category.objects.all()
    }


# View for the home page
def all_products(request):

    products = Product.objects.all()
    
    return render(request, 'store/home.html', {
        'products': products
        })


# View for the product detail page
def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug, in_stock=True)

    return render(request, 'store/products/detail.html', {
        'product': product
        })

# View for the category list
def category_list(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(request, 'store/products/category.html', {
        'category': category,
        'products': products
        })