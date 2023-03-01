from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

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

    context = {'videos':videos}
    return render(request, 'website/pages/works.html', context)

def materials(request):
    products = Product.objects.all()

    context = {'products':products}
    return render(request, 'website/pages/materials.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product':product}
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
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date']
        )
        return redirect('/')
        
    today = datetime.datetime.now()
    start = today.strftime('%Y-%m-%d')
    tomorrow = today + datetime.timedelta(days=1)
    end = tomorrow.strftime('%Y-%m-%d')
    next_year = today + datetime.timedelta(days=365)
    max = next_year.strftime('%Y-%m-%d')

    context = {'product':product, 'start':start, 'end':end, 'max':max}
    return render(request, 'website/pages/reserve.html', context)


def about(request):
    return render(request, 'website/pages/about.html')

def contact(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            # messages.success(request, 'Your message has been sent')

    return render(request, 'website/pages/contact.html')

def login(request):
    return render(request, 'website/pages/admin-login.html')

def dashboard(request):
    return render(request, 'website/pages/admin-dashboard.html')

# ADMIN SIDE

# PRODUCT
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
            return redirect('/products-list')

    context = {}
    return render(request, 'website/pages/admin-add-product.html', context)

# NEED TO UPDATE THIS VIEW TO DEAL WITH UPDATING MULTIPLE IMAGES
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        # images = request.FILES.getlist('images')
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products-list')

    context = {'product':product}
    return render(request, 'website/pages/admin-update-product.html', context)

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/products-list')

    context = {'product':product}
    return render(request, 'website/pages/admin-delete-product.html', context)

def products_list(request):
    # PAGINATION
    p = Paginator(Product.objects.all(), 2)
    page = request.GET.get('page')
    products = p.get_page(page)

    # SEARCH BAR
    search_contains_query = request.GET.get('search')

    if search_contains_query != '' and search_contains_query is not None:
        products = Product.objects.all().filter(
            Q(name__icontains=search_contains_query) |
            Q(category__icontains=search_contains_query)
        )

    context = {'products':products}
    return render(request, 'website/pages/admin-products-list.html', context)

def product_info(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product':product}
    return render(request, 'website/pages/admin-product-info.html', context)


# VIDEO
def add_video(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'video added with success')
            return redirect('/videos-list')

    context = {}
    return render(request, 'website/pages/admin-add-video.html', context)

def delete_video(request, pk):
    video = Video.objects.get(id=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('/videos-list')

    context = {'video':video}
    return render(request, 'website/pages/admin-delete-video.html', context)

def videos_list(request):
    # videos = Video.objects.all()
    showreel = Showreel.objects.first()

    # PAGINATION
    p = Paginator(Video.objects.all(), 2)
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

    context = {'videos':videos, 'showreel':showreel}
    return render(request, 'website/pages/admin-videos-list.html', context)

def update_showreel(request):
    showreel = Showreel.objects.first()
    form = ShowreelForm(instance=showreel)
    if request.method == 'POST':
        form = ShowreelForm(request.POST, request.FILES, instance=showreel)
        if form.is_valid():
            form.save()
            return redirect('/videos-list')
        
    context = {}
    return render(request, 'website/pages/admin-update-thumbnail.html', context)


# RESERVATION
def reservations_list(request):
    products = Product.objects.all()

    # PAGINATION
    p = Paginator(Reservation.objects.all(), 1)
    page = request.GET.get('page')
    reservations = p.get_page(page)

    search_contains_query = request.GET.get('search')

    if search_contains_query != '' and search_contains_query is not None:
        reservations = Reservation.objects.all().filter(
            Q(client_name__icontains=search_contains_query) |
            Q(product__name__icontains=search_contains_query) |
            Q(product__category__icontains=search_contains_query)
        )

    context = {'reservations': reservations, 'products': products}
    return render(request, 'website/pages/admin-reservations-list.html', context)

def reservation_details(request, pk):
    reservation = Reservation.objects.get(id=pk)

    context = {'reservation':reservation}
    return render(request, 'website/pages/admin-reservation-details.html', context)

def delete_reservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('/reservations-list')

    context = {'reservation':reservation}
    return render(request, 'website/pages/admin-delete-reservation.html', context)

# MESSAGE
def messages(request):
    messages = Message.objects.all().order_by('-date_sent')
    # clients = Client.objects.all()

    context = {'messages':messages}
    return render(request, 'website/pages/admin-messages.html', context)

# def send_message(request):
