import requests 
import json
import uuid

from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage


from techbro.models import Category,Dish, Showcase
from techbro.forms import SignupForm
from dashboard.models import Profile
from cart.models import *
from dashboard.forms import ProfileUpdateForm
from django.core.mail import EmailMessage

# password reset modules 
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q 
from django.utils.http import urlsafe_base64_encode 
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes 
# password reset modules
# from techbro.models import *import all models from models .py file here 
# Create your views here.
def index(request):
    # query the database to pull objects out 
    # all(){query to pull all objects in a particular model}
    # get query to pull one object
    # filter to pull out a group of objects 
    # [:no] to have specific number
    categories = Category.objects.all()   
    specials = Dish.objects.filter(special=True)
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)



    context = {
        'categories' :categories,
        'specials' :specials,
        'slide1' :slide1,
        'slide2' :slide2,
        'slide3' :slide3,
    }
    return render(request, 'index.html', context)
# password reset request 
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            for user in associated_users:
                subject = "Password Reset Requested"
                email_template_name = "password/password_reset_email.txt"
                c = {
                    "email":user.email,
                    # 'domain':'127.0.0.1:8000',
                    'domain':'54.83.87.115',
                    'site_name': 'Refill',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token' : default_token_generator.make_token(user),
                    'protocol' : 'http',
                }
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'okunsuwafejiro@gmail.com', [user.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect("password_reset/done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={
        "password_reset_form":password_reset_form
    })
# def contact(request):
#     return HttpResponse('okay')

def contact(request):
    return render(request, 'contact.html')

def category(request):
    all_meals = Dish.objects.all()
    categories = Category.objects.all()
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)

    context = {
        'all_meals':all_meals,
        'slide1' :slide1,
        'slide2' :slide2,
        'slide3' :slide3,
        'categories' :categories,
    }
    return render(request,'category.html',context )

def all_food(request):
    all_meals = Dish.objects.all()
    categories = Category.objects.all()
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)

    context = {
        'all_meals':all_meals,
        'slide1' :slide1,
        'slide2' :slide2,
        'slide3' :slide3,
        'categories' :categories,

    }

    return render(request, 'all_food.html',context)

def singlecat(request, id):
    categories = Category.objects.all()
    specials = Dish.objects.filter(special=True)
    singlecat = Dish.objects.filter(category_id = id)
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)
    cat_title = Category.objects.get(pk=id)


    context = {
        'specials' :specials,
        'categories' :categories,
        'singlecat': singlecat,
        'slide1' :slide1,
        'slide2' :slide2,
        'slide3' :slide3,
        'cat_title' : cat_title,


    }

    return render(request, 'singlecat.html',context)

def detail(request, id):
    categories = Category.objects.all()
    specials = Dish.objects.filter(special=True)
    # singlecat = Dish.objects.filter(category_id = id)
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=3)
    specials = Dish.objects.filter(special=True)
    detail = Dish.objects.get(pk=id)


    context = {
        'specials' :specials,
        'categories' :categories,
        # 'singlecat': singlecat,
        'slide1' :slide1,
        'slide2' :slide2,
        'slide3' :slide3,
        'specials' :specials,
        'detail' :detail,


    }
    return render(request, 'detail.html',context)

def signout(request):
    logout(request)
    messages.success(request, 'You have now signed out successfully!')
    return redirect('signin')

def signin(request):
    if request.method == "POST":
        myusername = request.POST['username']
        mypassword = request.POST['password']
        user = authenticate(request, username = myusername, password = mypassword)
        if user:
            login(request, user)
            messages.success(request, f'Dear {user.username}, your signin is successful, welcome')
            return redirect('index')
        else:
            messages.warning(request, 'Username/Password is incorrect')
            return redirect('signin')
    return render(request, 'signin.html')




def signup(request):
    # make a get request to pull out and display the SignupForm
    form = SignupForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        image = request.POST['image']
        form = SignupForm(request.POST)#instantiate the SignupForm for a POST request#
        if form.is_valid():#test form for virus fee, and declare valid#
            userform = form.save()#save incoming data#
            newuser = Profile(user = userform)
            newuser.first_name = userform.first_name
            newuser.last_name = userform.last_name
            newuser.email = userform.email
            newuser.phone = phone
            newuser.profile_pix = image
            newuser.save()
            messages.success(request, 'Signup successful')#send success message to your user#
            login(request, userform)
            return redirect('index')#redirect the user to any page of your choice#
        else:
            messages.error(request, form.errors)#send out error message(s)#
            return redirect('register')#if error occurs at signup attempt, keep user on signup page #

    return render(request, 'register.html')


@login_required(login_url='signin')
def profile(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    
    context = {
    'profile_data':profile_data
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='signin')
def profileupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update successful ')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profileupdate')

    context = {
        'form': form,
        'profile_data' : profile_data,
    }
    return render(request, 'profileupdate.html', context)

@login_required(login_url='signin')
def passwordupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('passwordupdate')
    context = {
        'profile_data':profile_data,
        'form':form,
    }
    return render(request, 'profilepassword.html', context)

# dashboard done

# shopcart
@login_required(login_url ='signin')
def ordermeal(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    cart_no = profile_data.id
    if request.method == 'POST':
        quantityselected = int(request.POST['mealquantity'])
        meal = request.POST['mealid']
        mealselected = Dish.objects.get(pk=meal)
        cart = Shopcart.objects.filter(user__username= request.user.username, paid=False)
        if cart:
            basket = Shopcart.objects.filter(dish=mealselected.id, user__username= request.user.username, paid=False).first()
            if basket:
                basket.quantity += quantityselected
                basket.amount = basket.quantity * basket.c_price
                basket.save()
                messages.success(request, 'Your meal is being processed! ')
                redirect('all_food')
            else:
                neworder = Shopcart()
                neworder.user = request.user
                neworder.dish = mealselected 
                neworder.c_name = mealselected.name 
                neworder.quantity = quantityselected 
                neworder.c_price = mealselected.price
                neworder.amount = mealselected.price * quantityselected
                neworder.cart_code = cart_no
                neworder.paid = False
                neworder.save()
                messages.success(request, 'Your meal is being proccessed!')
                return redirect('all_food')
        else:
            newitem = Shopcart()
            newitem.user = request.user
            newitem.dish = mealselected
            newitem.c_name = mealselected.name
            newitem.quantity = quantityselected
            newitem.c_price = mealselected.price
            newitem.amount = mealselected.price *quantityselected
            newitem.cart_code = cart_no
            newitem.paid = False
            newitem.save()
            messages.success(request, 'Your Meal is being processed!. ')
    return redirect('all_food')

@login_required(login_url='signin')
def mycart(request):
    profile = Profile.objects.get(user__username = request.user.username)
    shopcart = Shopcart.objects.filter(user__username = request.user.username, paid=False)
    
    subtotal = 0
    vat = 0
    total = 0
    
    for item in shopcart:
        subtotal += item.amount

    #7.5% of subtotal
    vat = 0.075 * subtotal

    total = vat + subtotal

    context = {
        'profile' :profile,
        'shopcart' :shopcart,
        'subtotal' :subtotal,
        'vat' :vat,
        'total' :total,
    }
    return render(request, 'cart.html', context)

@login_required(login_url='signin')
def decrease(request):
    if request.method == 'POST':
        itemquantity = int(request.POST['decrease'])
        cartitem = request.POST['itemid']
        decreasecart = Shopcart.objects.get(pk= cartitem)
        decreasecart.quantity -= itemquantity
        decreasecart.amount = decreasecart.c_price * decreasecart.quantity
        decreasecart.save()
        messages.success(request, 'Quantity decreased.')
        
    return redirect('mycart')
# increase cart quantity 

@login_required(login_url='signin')
def increase(request):
    if  request.method == 'POST':
        itemquantity = int(request.POST['increase'])
        cartitem = request.POST['itemid']
        increasecart = Shopcart.objects.get(pk= cartitem)
        increasecart.quantity += itemquantity
        increasecart.amount = increasecart.c_price * increasecart.quantity
        increasecart.save()
        messages.success(request, 'Quantity increased')

    return redirect('mycart')
# increase cart quantity 

def deletemeal(request):
    if request.method == 'POST':
        meal = request.POST['dishid']
        deletedish = Shopcart.objects.get(pk=meal)
        deletedish.delete()
        messages.success(request, 'Meal item deleted successfully.')
    return redirect('mycart')
    
def deleteallmeal(request):
    if request.method == 'POST':
        cleardish = Shopcart.objects.filter(user__username = request.user.username)
        cleardish.delete()
        messages.success(request, 'Cart cleared successfully.')
    return redirect('mycart')
# shopcart done 

def checkout(request):
    profile = Profile.objects.get(user__username = request.user.username)
    shopcart = Shopcart.objects.filter(user__username = request.user.username, paid=False)
    
    subtotal = 0
    vat = 0
    total = 0
    
    for item in shopcart:
        subtotal += item.amount

    #7.5% of subtotal
    vat = 0.075 * subtotal

    total = vat + subtotal

    context = {
        'profile' :profile,
        'shopcart' :shopcart,
        'subtotal' :subtotal,
        'vat' :vat,
        'total' :total,
    }
    return render(request, 'checkout.html', context)

# http://127.0.0.1:8000/completed
def payment(request):
    if request.method == 'POST': #integrate to paystack
        api_key = 'sk_test_59d24b82e82f1d27ace3b0ec221598d3981e2247'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://54.83.87.115/completed'
        ref_code =str( uuid.uuid4())
        user = User.objects.get(username = request.user.username)
        email = user.email
        profile = Profile.objects.get(user__username = request.user.username)
        cart_code = profile.id 
        total = float(request.POST['total']) * 100
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        new_email = request.POST['email']

        headers = {'Authorization': f'Bearer {api_key}'}#pass in the test key 
        data = {'reference':ref_code, 'amount': int(total), 'order_number':cart_code, 'email': email, 'callback_url':cburl}
 
        
        try:#make call to paystack
            r = requests.post(curl, headers=headers, json=data)#pip install requests
        except Exception:
            messages.error(request, 'Network busy, refresh and try again')
        else:
            transback = json.loads(r.text)#import json, import requests
            rurl = transback['data']['authorization_url']

            account = Payment()
            account.user = user
            account.first_name = fname
            account.last_name = lname
            account.phone = phone
            account.total = total/100
            account.cart_code = cart_code
            account.pay_code = ref_code
            account.address = address
            account.city = city
            account.paid = True
            account.save()

            email = EmailMessage(
                'Hello',#Title
                f'Dear {fname},  your order is confirmed! \n your delivery is in one hour. \n \n Thank you for your patronage.',#content
                settings.EMAIL_HOST_USER, #company email
                [new_email]#client email
            )

            email.fail_silently = True
            email.send()

            return redirect(rurl)
    return redirect('checkout')

def completed(request):
    profile = Profile.objects.get(user__username = request.user.username)
    cart = Shopcart.objects.filter(user__username = request.user.username, paid=False)

    for item in cart:
        item.paid = True
        item.save()

        stock = Dish.objects.get(pk = item.dish.id)
        stock.max -= item.quantity
        stock.save()
        
        context = {
            'profile' :profile
        }
    return render(request, 'completed.html')