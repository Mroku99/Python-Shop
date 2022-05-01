from django.shortcuts import render
from django.core.mail import send_mail

from .models import OrderItem, Order
from .forms import OrderForm
from .mail_sending import order_created_mail


from cart.cart import Cart

# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            order_created_mail(order.id)
            return render(request, 'order/created_order.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'cart': cart,
                                                       'form': form})

