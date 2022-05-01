from .models import Order
from django.core.mail import send_mail

def order_created_mail(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order number {order.id}'
    message = f'Hello {order.first_name} {order.last_name}\n\nThanks for shopping in our Python Shop. Order ID: {order.id}'
    return send_mail(subject, message, 'PythonShop@admin.com', [order.email])

