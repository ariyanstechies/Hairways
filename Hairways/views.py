from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from Hairways.models import Salons, Services, Owners, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import collections
import json
from django.core import serializers


def home(request):
    # To be revisited
    filtered_salons = Salons.objects.all().order_by('shares')
    # for pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(filtered_salons, 10)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {"salons": salons})


def locations(request):
    print("I was activated")
    # filtered_salons = Salons.objects.all().order_by('shares')
    if request.method == 'GET' and request.is_ajax():
        # For getting Salons within a selected location
        selected_location = request.GET.get('location', False)
        if selected_location == "All Locations":
            filtered_salons = Salons.objects.all().order_by('shares')
            print("selected_location is %s" % selected_location)
        else:
            filtered_salons = Salons.objects.filter(
                location=selected_location).order_by('shares')
            print("selected_location is again %s" % selected_location)
    # for pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(filtered_salons, 10)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)
    # some wired error happens if use json.dumps() directly.
    JsonInfoData = serializers.serialize("json", salons)

    # tmp = collections.OrderedDict()

    # change the str format to json format.
    # tmp['salons'] = json.loads(JsonInfoData)
    return HttpResponse(json.dumps(json.loads(JsonInfoData)))


def faqs(request):
    return render(request, "faqs.html")


def blog(request):
    return render(request, "blog.html")


def about(request):
    return render(request, "about.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        "form": form})


# protecting views you can't just access dashboard without logging
@login_required
def dashboard(request, id):
    owner = Salons.objects.get(id=id)
    return render(request, "dashboard/dashboard.html", {'owner': owner})


@login_required  # protecting views
def user(request, id):
    user_details = Owners.objects.get(ownerId=id)
    salon_details = Salons.objects.get(ownerId=id)
    return render(request, "dashboard/user.html", {'user_details': user_details, 'salon_details' : salon_details})


def productsServices(request):
    return render(request, "dashboard/productsServices.php")


@login_required
def staffClients(request):
    return render(request, "dashboard/staffClients.php")


@login_required
def map(request):
    return render(request, "dashboard/map.php")


@login_required
def calendar(request):
    return render(request, "dashboard/calendar.php")


@login_required
def upgrade(request):
    return render(request, "dashboard/upgrade.php")


def pricing(request):
    return render(request, "pricing.html")


def moreinfo(request, id):
    salon = Salons.objects.get(id=id)
    services = Services.objects.all()
    products = Products.objects.all()
    return render(request, "moreinfo.html", {'salon': salon, 'services' : services, 'products' : products})


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


#   TO BE REVIEWED DISPLAYS IMAGES
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'book_list.html', {
#         'books': books
#     })
#
#
# def delete_book(request, pk):
#     if request.method == 'POST':
#         book = Book.objects.get(pk=pk)
#         book.delete()
#     return redirect('book_list')
#
#
# class BookListView(ListView):
#     model = Book
#     template_name = 'class_book_list.html'
#     context_object_name = 'books'
