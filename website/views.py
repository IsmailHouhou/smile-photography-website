from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
import datetime


def home(request):
    showreel = Showreel.objects.first()
    videos = Video.objects.all()

    context = {'showreel':showreel, 'videos':videos}
    return render(request, 'website/index.html', context)

def services(request):
    return render(request, 'website/pages/services.html')

def works(request):
    videos = Video.objects.all()

    category = request.GET.get('category')

    if category:
        videos = videos.filter(category=category)

    context = {'videos':videos}
    return render(request, 'website/pages/works.html', context)

def materials(request):
    products = Product.objects.all()

    category = request.GET.get('category')

    if category:
        products = products.filter(category=category)

    context = {'products':products}
    return render(request, 'website/pages/materials.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    image_count = product.productimage_set.all().count()
    price_day_3 = product.price_day_3
    price_day_10 = product.price_day_10

    context = {'product':product, 'image_count':image_count, 'price_day_3':price_day_3, 'price_day_10':price_day_10}
    return render(request, 'website/pages/product.html', context)

def reserve(request, pk): # WORKING VERSION
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        reservation = Reservation.objects.create(
            product = product,
            client_name = request.POST['client_name'],
            client_email = request.POST['client_email'],
            client_address = request.POST['client_address'],
            client_business = request.POST['client_business'],
            client_prefix = request.POST['client_prefix'],
            client_phone = request.POST['client_phone'],
            client_status = request.POST['client_status'],
            read = 'False',
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date']
        )
        messages.success(request, 'Your reservation has been sent')
        return redirect('/')

    context = {'product':product}
    return render(request, 'website/pages/reserve.html', context)


def about(request):
    return render(request, 'website/pages/about.html')

def contact(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent')
            return redirect('/')

    return render(request, 'website/pages/contact.html')

# ADMIN SIDE
# LOGIN
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        message = ''
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                message = 'Username or Password incorrect'

        context = {'message':message}
        return render(request, 'website/pages/admin-login.html', context)

# LOGOUT
def logout_user(request):
    logout(request)
    return redirect('/')

# RESERVATION
def notification():
    if Reservation.objects.all().filter(read='False'):
        reservation_notif = 'True'
    else:
        reservation_notif = 'False'
    if Message.objects.all().filter(read='False'):
        message_notif = 'True'
    else:
        message_notif = 'False'

    return reservation_notif, message_notif

# DASHBOARD
@login_required(login_url='login')
def dashboard(request):
    reservation_notif, message_notif = notification()

    context = {'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-dashboard.html', context)

# PRODUCT
@login_required(login_url='login')
def add_product(request):
    form = ProductForm()
    image_form = ProductImageForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        if form.is_valid() and image_form.is_valid():
            f = form.save(commit=False)
            f.save()
            for image in images:
                ProductImage.objects.create(product=f, image=image)
            messages.success(request, 'Your product has been added')
            return redirect('/products-list')

    reservation_notif, message_notif = notification()
    context = {'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-add-product.html', context)

@login_required(login_url='login')
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    image_form = ProductImageForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        image_form = ProductImageForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        if form.is_valid() and image_form.is_valid():
            f = form.save(commit=False)
            f.save()
            if images:
                for product_image in product.productimage_set.all():
                    product_image.delete()
                for image in images:
                    ProductImage.objects.create(product=f, image=image)
            messages.success(request, 'Your product has been updated')
            return redirect('/products-list')

    reservation_notif, message_notif = notification()
    context = {'product':product, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-update-product.html', context)

@login_required(login_url='login')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.warning(request, 'Your product has been deleted')
        return redirect('/products-list')

    reservation_notif, message_notif = notification()
    context = {'product':product, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-delete-product.html', context)

@login_required(login_url='login')
def products_list(request):
    # PAGINATION
    p = Paginator(Product.objects.all(), 10)
    page = request.GET.get('page')
    products = p.get_page(page)

    # SEARCH BAR
    search_contains_query = request.GET.get('search')

    if search_contains_query != '' and search_contains_query is not None:
        products = Product.objects.all().filter(
            Q(name__icontains=search_contains_query) |
            Q(category__icontains=search_contains_query)
        )

    reservation_notif, message_notif = notification()
    context = {'products':products, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-products-list.html', context)

@login_required(login_url='login')
def product_info(request, pk):
    product = Product.objects.get(id=pk)

    reservation_notif, message_notif = notification()
    context = {'product':product, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-product-info.html', context)


# VIDEO
@login_required(login_url='login')
def add_video(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your video has been added')
            return redirect('/videos-list')

    reservation_notif, message_notif = notification()
    context = {'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-add-video.html', context)

@login_required(login_url='login')
def delete_video(request, pk):
    video = Video.objects.get(id=pk)
    if request.method == 'POST':
        video.delete()
        messages.warning(request, 'Your video has been deleted')
        return redirect('/videos-list')

    reservation_notif, message_notif = notification()
    context = {'video':video, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-delete-video.html', context)

@login_required(login_url='login')
def videos_list(request):
    showreel = Showreel.objects.first()

    # PAGINATION
    p = Paginator(Video.objects.all(), 10)
    page = request.GET.get('page')
    videos = p.get_page(page)

    search_contains_query = request.GET.get('search')

    if search_contains_query != '' and search_contains_query is not None:
        filter_arg = Q(title__icontains=search_contains_query) | Q(category__icontains=search_contains_query) | Q(client__icontains=search_contains_query)
        try:
            filter_arg |= Q(year=int(search_contains_query))
        except ValueError:
            pass
        videos = Video.objects.all().filter(filter_arg) 

    reservation_notif, message_notif = notification()
    context = {'videos':videos, 'showreel':showreel, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-videos-list.html', context)

@login_required(login_url='login')
def update_showreel(request):
    showreel = Showreel.objects.first()
    form = ShowreelForm(instance=showreel)
    if request.method == 'POST':
        form = ShowreelForm(request.POST, request.FILES, instance=showreel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your showreel has been updated')
            return redirect('/videos-list')
        
    reservation_notif, message_notif = notification()
    context = {'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-update-showreel.html', context)

@login_required(login_url='login')
def reservations_list(request):
    products = Product.objects.all()

    # PAGINATION
    p = Paginator(Reservation.objects.all().order_by('-order_date_time'), 10)
    page = request.GET.get('page')
    reservations = p.get_page(page)

    search_contains_query = request.GET.get('search')

    if search_contains_query != '' and search_contains_query is not None:
        reservations = Reservation.objects.all().order_by('-order_date_time').filter(
            Q(client_name__icontains=search_contains_query) |
            Q(product__name__icontains=search_contains_query) |
            Q(product__category__icontains=search_contains_query)
        )

    reservation_notif, message_notif = notification()
    context = {'reservations': reservations, 'products': products, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-reservations-list.html', context)

@login_required(login_url='login')
def reservation_details(request, pk):
    reservation = Reservation.objects.get(id=pk)
    reservation.read = 'True'
    reservation.save()

    reservation_notif, message_notif = notification()
    context = {'reservation':reservation, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-reservation-details.html', context)

@login_required(login_url='login')
def delete_reservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.warning(request, 'The selected reservation has been deleted')
        return redirect('/reservations-list')

    reservation_notif, message_notif = notification()
    context = {'reservation':reservation, 'reservation_notif':reservation_notif,'message_notif':message_notif}
    return render(request, 'website/pages/admin-delete-reservation.html', context)

# MESSAGE
@login_required(login_url='login')
def messages_page(request):
    messages = Message.objects.all().order_by('-date_time_sent')

    reservation_notif, message_notif = notification()
    context = {'messages':messages, 'reservation_notif':reservation_notif, 'message_notif':message_notif}
    return render(request, 'website/pages/admin-messages.html', context)

def update_message_read(request) :
    if request.method == 'POST':
        message_id = request.GET.get('message_id')
        message = Message.objects.get(id=message_id)
        message.read = 'True'
        message.save()

        return JsonResponse({'read': message.read})