
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail

from spices.models import Cart

# async def prvai():
#     for i in range(1, 100):
#         print(i)
#         print('vaishnavi')
#         await asyncio.sleep(1)
#     return True
        

# Create your views here.
@login_required(login_url='/register/')
def spices(request):
    
    cart = Cart.objects.get(user=request.user)
    cartitems = cart.cartitem_set.all()
    # use prvai
    # asyncio.run(prvai())
    for i in cartitems:
        print(i.product.name)
        print(i.quantity)

    return render(request, 'spices.html')

    # Send asynchronous email
    # send_mail(
    #     'your first email',
    #     'Your order placed succesfully.',
    #     'from mail',
    #     ['to_email'],
    #     fail_silently=False,
    # )





