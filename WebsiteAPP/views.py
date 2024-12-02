from django.shortcuts import render, redirect
from AdminApp.models import Product_DB, Catgory_DB
from WebsiteAPP.models import Contact_DB, Signup_DB, Cart_DB, Order_DB
from django.contrib import messages
import razorpay


def homepage(request):
    Cobj = Catgory_DB.objects.all()
    cartdata = Cart_DB.objects.filter(Sigin_Name=request.session['Sigin_Name'])
    count = cartdata.count()
    return render(request, 'home.html', {'Cobj': Cobj, 'count': count})


def productspage(request):
    Pobj = Product_DB.objects.all()
    return render(request, 'Products.html', {'Pobj': Pobj})


def contactpage(request):
    return render(request, 'contactdata.html')


def Save_Contact_DB(request):
    if request.method == 'POST':
        coa = request.POST.get('name')
        cob = request.POST.get('message')
        coc = request.POST.get('email')
        Coobj = Contact_DB(Contact_Name=coa, Contact_Email=coc, Contact_TextArea=cob)
        Coobj.save()
        return redirect(contactpage)


def display_contact_page(request):
    disp_cobj = Contact_DB.objects.all()
    return render(request, 'display_contact.html', {'disp_cobj': disp_cobj})


def filtered_product_page(request, Cat_name):
    data1 = Product_DB.objects.filter(Category_of_Product=Cat_name)
    return render(request, 'filtered_product.html', {'data1': data1})


def Single_product_page(request, prod_id):
    data = Product_DB.objects.get(id=prod_id)
    return render(request, 'single_product.html', {'data': data})


def signup_page(request):
    return render(request, 'signup.html')


def login_page(request):
    return render(request, 'login.html')


def save_Signup_DB(request):
    if request.method == "POST":
        sa = request.POST.get('name')
        sb = request.POST.get('email')
        sc = request.POST.get('mob')
        sd = request.POST.get('pass')
        se = request.POST.get('re_pass')
        Sigobj = Signup_DB(Sigin_Name=sa, Sigin_Email=sb, Sigin_Mobile=sc, Sigin_Pswd=sd, Sigin_confpswd=se)
        if Signup_DB.objects.filter(Sigin_Name=sa).exists():
            messages.warning(request, "user already exists..!!")
        elif Signup_DB.objects.filter(Sigin_Email=sb).exists():
            messages.warning(request, "email already exists..!!")
            return redirect(signup_page)
        Sigobj.save()
        messages.success(request, "your details are saved")
        return redirect(signup_page)


def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('your_name')
        pwd = request.POST.get('your_pass')
        if Signup_DB.objects.filter(Sigin_Name=un, Sigin_Pswd=pwd).exists():
            request.session['Sigin_Name'] = un
            request.session['Sigin_Pswd'] = pwd
            messages.success(request, "succesfully logged in ")
            return redirect(homepage)

        else:
            messages.error(request, "username or password doesnot exist ")
            return redirect(login_page)

    else:
        return redirect(login_page)


def user_logout(request):
    del request.session['Sigin_Name']
    del request.session['Sigin_Pswd']
    messages.success(request, "succesfully logged out ")
    return redirect(homepage)


def Save_Cart_DB(request):
    if request.method == "POST":
        ca = request.POST.get('tquantity')
        cb = request.POST.get('perprice')
        cc = request.POST.get('totprice')
        cd = request.POST.get('productname')
        ce = request.POST.get('tsiginname')

        try:
            x = Product_DB.objects.get(Product_Name=cd)
            img = x.Product_Image1
        except Product_DB.DoesNotExist:
            img = None

        Carobj = Cart_DB(No_of_orders=ca, Price_Per_Quantity=cb, Total_price=cc, Product_Name=cd, Sigin_Name=ce,
                         Prod_Img=img)
        Carobj.save()
        return redirect(cart_page)


def cart_page(request):
    currentusername = request.session.get('Sigin_Name')
    cartdata = Cart_DB.objects.filter(Sigin_Name=request.session['Sigin_Name'])
    SubTotal = 0
    ShippingCharge = 0
    for i in cartdata:
        SubTotal = SubTotal + i.Total_price
    if SubTotal > 1000:
        ShippingCharge = 100
    else:
        ShippingCharge = 300
    Final_Pay = SubTotal + ShippingCharge

    return render(request, 'cartpage.html',
                  {'cartdata': cartdata, 'SubTotal': SubTotal, 'ShippingCharge': ShippingCharge, 'Final_Pay': Final_Pay,
                   'currentusername': currentusername})


def check_outpage(request):
    currentusername = request.session.get('Sigin_Name')
    cartdata = Cart_DB.objects.filter(Sigin_Name=request.session['Sigin_Name'])
    SubTotal = 0
    ShippingCharge = 0
    for i in cartdata:
        SubTotal = SubTotal + i.Total_price
    if SubTotal > 1000:
        ShippingCharge = 100
    else:
        ShippingCharge = 300
    Final_Pay = SubTotal + ShippingCharge

    return render(request, 'check_outpage.html',
                  {'cartdata': cartdata, 'SubTotal': SubTotal, 'ShippingCharge': ShippingCharge,
                   'Final_Pay': Final_Pay, 'currentusername': currentusername})


def Save_Order_DB(request):
    if request.method == 'POST':
        oa = request.POST.get('tname')
        ox = request.POST.get('tmail')
        ob = request.POST.get('tplace')
        oc = request.POST.get('taddress')
        od = request.POST.get('tmobile')
        oe = request.POST.get('tmessage')
        of = request.POST.get('tsub')
        og = request.POST.get('tship')
        oi = request.POST.get('tfinal')
        orderobj = Order_DB(Name=oa, Email=ox, Place=ob, Address=oc, Mobile=od, Message=oe, Sub_Total=of,
                            Shipping_Price=og, Final_Pay=oi)
        orderobj.save()
        return redirect(paymentpage)


# Create your views here.

def paymentpage(request):
    customer = Order_DB.objects.order_by('-id').first()
    payy = customer.Final_Pay
    amount = int(payy * 100)
    payy_str = str(amount)
    # below line not required
    for i in payy_str:
        print(i)
    if request.method == "POST":
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_test_QTazbZdC0vhYg3', 'dVtHxomtAL4THQWFXuezm5eG'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})
    return render(request, 'paymentpage.html', {'customer': customer, 'payy_str': payy_str})
