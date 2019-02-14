from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from Hairways.models import Salons, Services, Owners, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..decorators import client_required
from ..decorators import owner_required
from django.http import HttpResponse
import json
from django.core import serializers
from django.views.generic import TemplateView


def home(request):
    # To be revisited
    filtered_salons = Salons.objects.all().order_by('likes')
    # for pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(filtered_salons, 10)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)

    # print("Holly shit %s" % salons.getItems) to be revisted
    return render(request, 'index.html', {"salons": salons })

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
@method_decorator([login_required, owner_required], name='dispatch')
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


def moreinfo(request, id):
    """django takes care of joins automatically. When we query everything in Salons
    we also get any related information by foreign key as well,
     But the way that we access this in html is a litle different.
      We have to go through the variable used as the foreign key to access the
       information associated with that join. e.g
       {% for x in data %}
       {{ x.salonName.serviceName }}
       {{ x.salonName.availability }} etc... easy right? :)
       {% endfor %}
       """
    salon = Salons.objects.get(id=id)
    services = Services.objects.filter(salons__salonName=salon.salonName)
    products = Products.objects.filter(salons__salonName=salon.salonName)
    return render(request, "moreinfo.html", {'salon': salon, 'services' : services, 'products' : products})

@csrf_exempt
def update_views(request):
    if request.method == 'POST' and request.is_ajax():
        get_view = request.POST.get('salonId', False)
        update_view = Salons.objects.get(id=get_view)
        update_view.views +=1
        update_view.save()
    return HttpResponse("Salon With ID %s Views Was Updated successfully" % update_view.views)

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


# def decider(request):
#     if request.user.is_authenticated:
#         if request.user.is_teacher:
#             return redirect('home_views:dashboard')
#         else:
#             return redirect('index.html')
#     return render(request, 'index.html')
