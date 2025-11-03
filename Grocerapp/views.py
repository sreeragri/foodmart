import razorpay
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import tbl_order, tbl_Delivery_partners

from .models import *
razorpay_client = razorpay.Client(auth=('rzp_test_9zruMnoLDlsCLG','oXUZ9Mf5zhjoZsTFLc7RpABO'))



# Create your views here.
def index(request,):
    categoryswiper=tbl_category.objects.all()
    allproductsview=tbl_Products.objects.all()
    popular = tbl_Products.objects.all()[:6]
    just = tbl_Products.objects.all().order_by('-id')
    cart_item = tbl_cart.objects.filter(session_key=request.session.session_key)
    total_cart = sum(item.total_price() for item in cart_item)
    total_count_cart = cart_item.count()
    return render(request,"index.html",{"categoryswiper":categoryswiper,"cart_item":cart_item,"total_cart":total_cart,"total_count_cart":total_count_cart,"allproductsview":allproductsview,"popular":popular,"just":just})
def Login(request):
    return render(request,'Login.html')
def check_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/dashboard/")
        elif tbl_signup.objects.filter(Username=username, Password=password).exists():
            d = tbl_signup.objects.get(Username=username, Password=password)
            request.session['userid'] = d.id
            if tbl_cart.objects.filter(User=d.id).exists():
                return redirect("checkout")
            else:
                return redirect('/')
        elif tbl_Delivery_partners.objects.filter(Email=username, Password=password).exists():
            d = tbl_Delivery_partners.objects.get(Email=username, Password=password)
            request.session['del_id'] = d.id
            return redirect("/delivery_dashboard/")
        else:
            return redirect("/Login/")

def dashboard(request):
    return render(request, 'dashboard.html')
def categories(request):
    data=tbl_category.objects.all()

    return render(request,'categories.html',{'data':data})

def create_category(request):
    return render(request,'create categories.html')
def save_category(request):
    G=tbl_category()
    G.categoryname=request.POST.get('category-name')
    G.categoryimage=request.FILES.get('category-image')
    G.categorystatus=request.POST.get('category-status')
    G.save()
    return redirect("/create_category/")
def edit_category(request,id):
    data=tbl_category.objects.get(id=id)
    return render(request,'edit_category.html',{'data':data})

def delete_category(request,id):
    data=tbl_category.objects.get(id=id)
    data.delete()
    return redirect("/categories/")

def update_category(request,id):
    data=tbl_category.objects.get(id=id)
    data.categoryname=request.POST.get("category-name")
    if request.FILES.get("category-image"):
        data.categoryimage=request.FILES.get("category-image")
    data.categorystatus=request.POST.get("category- status")
    data.save()
    return redirect("/categories/")

def SubCategories(request):
    data1 = tbl_SubCategory.objects.all()
    return render(request,'SubCategories.html',{'data1':data1})

def create_SubCategory(request):
    data3=tbl_category.objects.all()

    return render(request,'create_SubCategories.html',{'data3':data3})

def save_SubCategory(request):
    S=tbl_SubCategory()
    S.category_id=request.POST.get('Category')
    S.SubCategoryname=request.POST.get('SubCategory-name')
    S.SubCategoryimage=request.FILES.get('SubCategory-image')
    S.SubCategorystatus=request.POST.get('SubCategory-status')
    S.save()
    return redirect("/create_SubCategory/")
def edit_SubCategory(request,id):
    data1=tbl_SubCategory.objects.get(id=id)
    data3=tbl_category.objects.all()

    return render(request,'edit_SubCategory.html',{'data1':data1,'data3':data3})
def delete_SubCategory(request,id):
    data1=tbl_SubCategory.objects.get(id=id)
    data1.delete()
    return redirect("/SubCategories/")
def update_SubCategory(request,id):
    data1=tbl_SubCategory.objects.get(id=id)

    data1.SubCategoryname=request.POST.get('SubCategory-name')
    if request.FILES.get("SubCategory-image"):
        data1.SubCategoryimage=request.FILES.get("SubCategory-image")
    data1.SubCategorystatus=request.POST.get('SubCategory-status')
    data1.save()
    return redirect('/SubCategories/')

def Products(request):
    data2=tbl_Products.objects.all()
    return render(request,'Products.html',{'data2':data2})

def create_products(request):
    data4=tbl_category.objects.all()
    data5=tbl_SubCategory.objects.all()

    return render(request,'create_products.html',{'data4':data4,'data5':data5})

def save_products(request):
    P=tbl_Products()
    P.category_id=request.POST.get('Category')
    P.SubCategory_id=request.POST.get('SubCategory')
    P.Productname=request.POST.get('Product-name')
    P.Productimage=request.FILES.get('Product-image')
    P.Productprice=request.POST.get('Product-price')
    P.Productofferprice=request.POST.get('Product-offerprice')
    P.Productweight=request.POST.get('Product-weight')
    P.Productdescription=request.POST.get('Product-description')
    P.ProductNumofpieces=request.POST.get('Product-Numofpieces')
    P.ProductStockin=request.POST.get('Product-Stockin')
    P.ProductStockout=request.POST.get('Product-Stockout')

    P.save()
    return redirect('/create_products/')

def delete_Products(request,id):
    data2=tbl_Products.objects.get(id=id)
    data2.delete()
    return redirect("/Products/")

def edit_Products(request,id):
    data2=tbl_Products.objects.get(id=id)
    cat=tbl_category.objects.all()
    sub=tbl_SubCategory.objects.all()
    return render(request,'edit_Products.html',{'data2':data2,"cat":cat,"sub":sub})

def update_products(request,id):
    data2=tbl_Products.objects.get(id=id)
    data2.Productname=request.POST.get('Product-name')
    if request.FILES.get('Product-image'):
        data2.Productimage=request.FILES.get('Product-image')
    data2.Productprice=request.POST.get('Product-price')
    data2.Productofferprice=request.POST.get('Product-offerprice')
    data2.Productweight=request.POST.get('Product-weight')
    data2.Productdescription=request.POST.get('Product-description')
    data2.ProductNumofpieces=request.POST.get('Product-Numofpieces')
    data2.ProductStockin=request.POST.get('Product-Stockin')
    data2.ProductStockout=request.POST.get('Product-Stockout')

    data2.save()
    return redirect('/Products/')

def Cat_Products(request,id):
    CP=tbl_SubCategory.objects.filter(category=id)
    CP1=tbl_Products.objects.filter(category=id)
    cart_item=tbl_cart.objects.filter(session_key=request.session.session_key)
    total_cart=sum(item.total_price() for item in cart_item)
    total_count_cart=cart_item.count()
    return render(request,'Cat_Products.html',{'CP':CP,'CP1':CP1,"cart_item":cart_item,"total_cart":total_cart,"total_count_cart":total_count_cart})



def SubCatProducts(request,id):
    SCP=tbl_Products.objects.filter(SubCategory=id)
    sub=tbl_SubCategory.objects.get(id=id)
    all_sub=tbl_SubCategory.objects.filter(category=sub.category.id)

    cart_item = tbl_cart.objects.filter(session_key=request.session.session_key)
    total_cart = sum(item.total_price() for item in cart_item)
    total_count_cart = cart_item.count()

    return render(request,"SubCatProducts.html",{"SCP":SCP,"all_sub":all_sub,"sub":sub,"cart_item":cart_item,"total_cart":total_cart,"total_count_cart":total_count_cart})

def add_to_cart(request, id):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    product = tbl_Products.objects.get(id=id)

    cart_item, created = tbl_cart.objects.get_or_create(
        session_key=session_key,
        Product=product,
        defaults={'Quantity': 1}
    )
    if not created:
        cart_item.Quantity += 1
        cart_item.save()
    tbl_wishlist.objects.filter(Product=id).delete()

    # Add success message
    messages.success(request, f"{product.Productname} added to cart!")

    # Redirect to previous page
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return HttpResponseRedirect(referer)
    else:
        return redirect('/')

def wishlist(request):
    SCP=tbl_wishlist.objects.filter(session_key=request.session.session_key)
    cart_item = tbl_cart.objects.filter(session_key=request.session.session_key)
    total_cart = sum(item.total_price() for item in cart_item)
    total_count_cart = cart_item.count()

    return render(request,"wishlist.html",{"SCP":SCP,"cart_item":cart_item,"total_cart":total_cart,"total_count_cart":total_count_cart})

def add_to_wishlist(request,id):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    product = tbl_Products.objects.get(id=id)

    cart_item, created = tbl_wishlist.objects.get_or_create(
        session_key=session_key,
        Product=product,
    )
    return redirect('/wishlist/')

def checkout(request):
    cart_items = tbl_cart.objects.filter(session_key=request.session.session_key)
    total_price = sum(item.total_price() for item in cart_items)
    currency = 'INR'
    amount = int(total_price) * 100
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']


    # we need to pass these details to frontend.
    context = {}


    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = 'rzp_test_9zruMnoLDlsCLG'
    context['razorpay_amount'] = amount
    context['currency'] = currency

    context['cart_items'] = cart_items
    context['total_price'] = total_price





    return render(request, 'checkout.html',context)


def signup(request):
    return render(request,"signup.html")

def save_signup(request):
    Sign=tbl_signup()
    Sign.Username=request.POST.get('Username')
    Sign.Mobile=request.POST.get('Mobile')
    Sign.Password=request.POST.get('Password')
    Sign.save()
    return redirect('/Login/')

def save_order(request):
    order=tbl_order()
    order.Fullname=request.POST.get('Fullname')
    order.Address=request.POST.get('Address')
    order.Phonenumber=request.POST.get('Phonenumber')
    order.Paymentmethod=request.POST.get('Paymentmethod')
    order.User_id=request.session['userid']
    cart_item = tbl_cart.objects.filter(session_key=request.session.session_key)
    total_cart = sum(item.total_price() for item in cart_item)
    order.Total_price=total_cart
    order.save()
    for i in cart_item:
        item=tbl_order_item()
        item.Product_id=i.Product.id
        item.Quantity=i.Quantity
        item.User_id=request.session['userid']
        item.session_key=i.session_key
        item.order_id=order.id
        item.save()
    cart_item.delete()


    razorpay_order_id = request.POST.get('order_id')
    payment_id = request.POST.get('payment_id', '')
    signature = request.POST.get('razorpay_signature', '')
    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }
    # verify the payment signature.
    amount = int(total_cart) *100  # Rs. 200


    razorpay_client.payment.capture(payment_id, amount)
    return redirect("/")

def Admin_Orders(request):
    orders = tbl_order.objects.all().order_by('-id')
    order_items = tbl_order_item.objects.select_related('Product', 'order').all()

    assignments = Tbl_order_assign.objects.select_related('partner_id', 'order_id').all()

    delivery_mapping = {assign.order_id: assign.partner_id for assign in assignments}
    print(delivery_mapping)

    return render(request, 'Admin_Orders.html', {
        'orders': orders,
        'order_items': order_items,
        'delivery_mapping': delivery_mapping,
    })
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(tbl_order, id=order_id)
        new_status = request.POST.get('Status')
    if new_status in ['Out for Delivery', 'Cancelled']:
        order.Status = new_status
        order.save()
    return redirect('/Admin_Orders/')

def Delivery_partners(request):
    DelPartner = tbl_Delivery_partners.objects.all()

    return render(request,"Delivery_partner.html",{'DelPartner':DelPartner})
def create_delivery_partner(request):

    return render(request,'create_delivery_partner.html')

def save_delivery_partners(request):
    SDP=tbl_Delivery_partners()
    SDP.Name=request.POST.get('Name')
    SDP.Contact=request.POST.get('Contact')
    SDP.Age=request.POST.get('Age')
    SDP.Address=request.POST.get('Address')
    SDP.Vehicledetails=request.POST.get('vehicle-details')
    SDP.Email=request.POST.get('dely-Email')
    SDP.Password=request.POST.get('dely-Password')
    SDP.save()
    return redirect("/create_delivery_partner/")
def edit_deliverypartner(request,id):
    DelPartner = tbl_Delivery_partners.objects.get(id=id)
    return render(request,'edit_deliverypartner.html',{'DelPartner':DelPartner})

def update_deliverypartner(request,id):
    DelPartner = tbl_Delivery_partners.objects.get(id=id)
    DelPartner.Name = request.POST.get('Name')
    DelPartner.Contact = request.POST.get('Contact')
    DelPartner.Age = request.POST.get('Age')
    DelPartner.Address = request.POST.get('Address')
    DelPartner.Vehicledetails = request.POST.get('vehicle-details')
    DelPartner.Email=request.POST.get('dely-Email')
    DelPartner.Password=request.POST.get('dely-Password')
    DelPartner.save()
    return redirect('/Delivery_partners/')

def delete_deliverypartner(request,id):
    DelPartner = tbl_Delivery_partners.objects.get(id=id)
    DelPartner.delete()
    return redirect('/Delivery_partner/')



def out_for_delivery_page(request,id):
    orders = tbl_order.objects.get(id=id)
    partners = tbl_Delivery_partners.objects.all()
    return render(request, 'out_for_delivery_page.html', {'orders': orders,'partners': partners})


def assign_delivery_partner(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        partner_id = request.POST.get('partner_id')
        order = get_object_or_404(tbl_order, id=order_id)
        partner = get_object_or_404(tbl_Delivery_partners, id=partner_id)
        order.Status = 'Out for Delivery'
        order.save()
        OFD=Tbl_order_assign()
        OFD.partner_id=partner
        OFD.order_id=order
        OFD.save()
        subject="delivery Notification"
        message="An order is ready for pickup"
        send_mail(subject,message,settings.EMAIL_HOST_USER,[partner.Email])


        return redirect('/Admin_Orders/')

def delivery_dashboard(request):
    return render(request, 'delivery_dashboard.html')

def delivery_orders(request):
    delorder=Tbl_order_assign.objects.filter(partner_id=request.session['del_id'])
    order_items = tbl_order_item.objects.select_related('Product', 'order').all()



    return render(request,'delivery_orders.html',{'delorder':delorder,'order_items':order_items})

def ordercomplete(request,id):
    ODC=tbl_order.objects.get(id=id)
    ODC.Status='completed'
    ODC.save()
    return redirect('/delivery_orders/')
def ordercancel(request,id):
    OC=tbl_order.objects.get(id=id)
    OC.Status='Cancelled'
    OC.save()
    return redirect('/delivery_orders/')
def logoutpartner(request):
    del request.session['del_id']
    return redirect('/')

def Contactpage(request):
    return render(request,'Contactpage.html')

def save_contactpage(request):
    Cpage=Tbl_contact_page()
    Cpage.contactname=request.POST.get('name')
    Cpage.email=request.POST.get('email')
    Cpage.subject=request.POST.get('subject')
    Cpage.message=request.POST.get('message')
    Cpage.save()
    return redirect("/Contactpage/")

def contactpagetbl(request):
    Data= Tbl_contact_page.objects.all()
    return render(request,'contactpagetbl.html',{'Data':Data})
def Logout(request):
    logout(request)
    return redirect ('/')
def myaccount(request):
    user=tbl_signup.objects.get(id=request.session['userid'])
    order=tbl_order.objects.filter(User=request.session['userid'])
    return render(request,'myaccount.html',{'user':user,'order':order})
def Logout_user(request):
    del request.session['userid']
    return redirect('/')


























































