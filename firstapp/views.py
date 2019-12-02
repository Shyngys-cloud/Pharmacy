from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, JsonResponse
from firstapp.models import  Category, Product, CartItem, Cart, Order
from django.core.urlresolvers import reverse
from decimal import Decimal
from firstapp.forms import OrderForm, SearchForm, RegisterForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.auth import  login
from django.contrib.auth import authenticate, login as dj_login



def base_view(request):

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'username': auth.get_user(request).username
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total']=cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'categories': categories,
        'cart': cart,
        'username': auth.get_user(request).username
        }
    return render (request, 'product.html', context)

def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories
        }
    return render (request, 'category.html', context)

def cart_view (request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total']=cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'cart':cart
    }
    return render(request, 'cart.html', context)

def add_to_cart_view (request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total']=cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.item.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({'cart_total':cart.item.count(), 'cart_total_price': cart.cart_total})

def remove_from_cart_view (request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total']=cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart(product_slug)
    new_cart_total = 0.00
    for item in cart.item.all():
        new_cart_total += float(item.item_total)
    cart.cart_total= new_cart_total
    cart.save()
    return JsonResponse({'cart_total': cart.item.count(), 'cart_total_price': cart.cart_total})
def change_item_qty(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    qty = request.GET.get('qty')
    item_id = request.GET.get('item_id')
    cart_item = CartItem.objects.get(id=int(item_id))
    cart.change_qty(qty, item_id)
    return JsonResponse(
        {'cart_total': cart.item.count(),
         'item_total': cart_item.item_total,
         'cart_total_price': cart.cart_total
         })
def checkout_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'cart':cart
        }
    return render(request, 'checkout.html', context)

def order_create_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = OrderForm(request.POST or None)
    context = {
        'form':form
    }
    return  render(request, 'order.html', context)

def make_order_view(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        buying_type = form.cleaned_data['buying_type']
        address = form.cleaned_data['address']
        comments = form.cleaned_data['comments']
        new_order = Order()
        new_order.user = request.user
        new_order.save()
        new_order.items.add(cart)
        new_order.first_name = name
        new_order.last_name = last_name
        new_order.phone = phone
        new_order.address = address
        new_order.buying_type = buying_type
        new_order.comments = comments
        new_order.total = cart.cart_total
        new_order.save()
        request.session['total'] = cart.item.count()
        del request.session['cart_id']
        del request.session['total']
        return render(request, 'thank_you.html')

def search(request):
    try:
        if request.method=="POST":
            product_name = request.POST.get("search_field")
            if len(product_name)>0:
                search_res = Product.objects.filter(name__contains=product_name)
                return render(request, "search.html",
                        {"search_res":search_res,"empty_res":"There is no good"})
    except:
        return render(request, "search.html",{"empty_res":"There is no good"})


def user_login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect("/")
        else:
            args['login_error'] = 'user is not found'
            return render_to_response ('login.html' ,args)
    else:
     return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")




def user_register(request):
    template = 'register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})