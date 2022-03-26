# [[1,2],[3,4]]
# send all the available products
# loop for making html list of items
# for post request fetch the data from the form
# Create your views here.
#     for i in range(1, 100):
#         print(i)
#         print('vaishnavi')
#         await asyncio.sleep(1)
#     return True
# send mail function
# async def prvai():
# from django.template.loader import render_to_string
# from threading import Thread
# from multiprocessing import context
# from email.message import EmailMessage
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail
import threading
from spices.models import Cart, CartItem, Product
from website.settings import EMAIL_HOST_USER


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        send_mail(self.subject, self.html_content, EMAIL_HOST_USER,
                  self.recipient_list, fail_silently=False, html_message=self.html_content)


def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()


@login_required(login_url='/register')
def spices(request):
    products = Product.objects.all()
    if request.method == 'POST':
        total = 0
        today = date.today()
        phone = request.POST['phone']
        address = request.POST['address']
        cart = Cart(user=request.user, phone=phone, address=address)
        cart.save()

        itemList = ''
        item_info = []

        for i in products:
            tar = int(request.POST[str(i.id)])
            if tar > 0:
                cartitem = CartItem(cart=cart, product=i, quantity=tar)
                cartitem.save()
                itemList += f'''<div class="total" style="box-sizing: border-box;padding: 12px 0;border-top: 2px dashed #ccc;">
							<span style="box-sizing: border-box; color: slategray;">{i.name} x {tar}</span>
							<span class="total_price" style="box-sizing: border-box;float: right;color: #db4a00;">₹ {int(tar) * i.price}</span>
						</div>'''
                k = int(tar) * i.price
                total += k
                item_info.append([i, int(tar), k])

        html_message = f'''
        <div class="container" style="box-sizing: border-box;border-radius: 5px;background-color: white;box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);z-index: 1;">
		<div class="receipt_box" style="box-sizing: border-box;">
			<div class="head" style="box-sizing: border-box;
			padding-top: 5px;
			" align="center">
				<div class="logo" style="box-sizing: border-box;flex: 1 0 30%; width: 20%;">
					<img src="https://raw.githubusercontent.com/Vaishnavi-N-08/AarshitiGroup/master/static/assets/Green-logo.png" style="box-sizing: border-box;width: 100%;">
				</div>
			</div>
			<div class="body" style="box-sizing: border-box;padding: 16px 32px;">
				<div class="total" style="box-sizing: border-box;padding: 12px 0;">
					<span style="box-sizing: border-box; color: slategray; font-weight: bold; color: chocolate;"><span style="color: black;">Hi, </span>{request.user.first_name}</span>
					<span class="total_price" style="box-sizing: border-box;float: right;color: slategray;">{today}</span>
				</div>
				<div class="total" style="box-sizing: border-box;padding: 12px 0;">
                <span style="box-sizing: border-box; color: slategray;"><span
                        style="color: black;">Contact: </span>{cart.phone}</span>
            </div>
            <div class="total" style="box-sizing: border-box;padding: 12px 0;">
                <span style="box-sizing: border-box; color: slategray;"><span
                        style="color: black;">Address: </span>{cart.address}</span>
            </div>
				<div class="cart" style="box-sizing: border-box;">
					<div class="title" style="box-sizing: border-box;margin-bottom: 16px;font-size: 20px;font-weight: bold;text-align: center;text-transform: capitalize;">cart</div>
					<div class="content" style="box-sizing: border-box;font-size: 14px;">
						{itemList}
						<div class="total" style="box-sizing: border-box;padding: 12px 0;font-weight: bold;text-transform: uppercase;border-top: 2px solid darkorange;">
							<span style="box-sizing: border-box;">total</span>
							<span class="total_price" style="box-sizing: border-box;float: right;color: #db4a00;">₹ {total}</span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	'''
        send_html_mail('Order Placed', html_message, [request.user.email])
        send_html_mail('Order Placed', html_message, ["admin@aarshitigroup.in"])
        flag = True
        context = {'flag': flag, 'total': total, 'today': today,
                   'item_info': item_info, 'cart': cart}
        return render(request, 'spices.html', context)
    else:
        context = {'spices': products}
        return render(request, 'spices.html', context)
