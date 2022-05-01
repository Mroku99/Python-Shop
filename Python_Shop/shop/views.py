from django.shortcuts import render, get_object_or_404

from .models import Category, Product

from cart.forms import CartAddProductForm

# PRODUCT LIST AND PRODUCT LIST BY CATEGORY
def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()

    if category_slug:
        category = Category.objects.filter(slug=category_slug)
        products = Product.objects.filter(category__in=category)

    return render(request, 'shop/product_list.html', {'products': products,
                                                      'category': category})

# PRODUCT DETAIL
def product_detail(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id, slug=product_slug)
    cart_form = CartAddProductForm()

    return render(request, 'shop/product_detail.html', {'product': product,
                                                        'cart_form': cart_form})

