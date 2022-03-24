
from email.message import EmailMessage
from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail
import threading
from threading import Thread
from spices.models import Cart, CartItem, Product
from website.settings import EMAIL_HOST_USER

# async def prvai():
#     for i in range(1, 100):
#         print(i)
#         print('vaishnavi')
#         await asyncio.sleep(1)
#     return True
        
# send mail function


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        # msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
        # msg.content_subtype = "html"
        # msg.send()

        send_mail(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list, fail_silently=False)

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()



# Create your views here.
@login_required(login_url='/register/')
def spices(request):
    # for post request fetch the data from the form
    products = Product.objects.all()
    if request.method == 'POST':
        total = 0
        cart = Cart(user=request.user)
        cart.save()
        for i in products:
            tar = int(request.POST[str(i.id)])  
            if tar > 0:
                cartitem = CartItem(cart=cart, product=i, quantity=tar)
                cartitem.save()
                total += int(tar) * i.price
        send_html_mail('Order Placed', '<h1>Order Placed</h1>', ['om.surushe20@vit.edu'])
        flag = True
        context = {'flag':flag, 'total':total}
        return render(request, 'spices.html', context)
    else:
        context = { 'spices': products }
        # send all the available products
        return render(request, 'spices.html', context)