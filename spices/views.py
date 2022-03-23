
from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail

from spices.models import Cart, CartItem, Product

# async def prvai():
#     for i in range(1, 100):
#         print(i)
#         print('vaishnavi')
#         await asyncio.sleep(1)
#     return True
        

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
        flag = True
        context = {'flag':flag, 'total':total}
        return render(request, 'spices.html', context)
    else:
        context = { 'spices': products }
        # send all the available products
        return render(request, 'spices.html', context)