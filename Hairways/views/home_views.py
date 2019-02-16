from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from Hairways.models import Salons, Services, Owner, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..decorators import client_required
from ..decorators import owner_required
from django.http import HttpResponse
import json
from django.core import serializers
from django.views.generic import TemplateView


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



# protecting views you can't just access dashboard without logging
@method_decorator([login_required, owner_required], name='dispatch')
def dashboard(request):
    owner = Salons.objects.all()
    return render(request, "dashboard/dashboard.html", {'owner': owner})


@login_required  # protecting views
def user(request, id):
    user_details = Owner.objects.get(ownerId=id)
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


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'



from django.views import generic

@method_decorator([login_required, owner_required], name='dispatch')
class AppointmentListView(generic.ListView):
    model = Salons
    context_object_name = 'my_salon'
    template_name = 'dashboard/dashboard.html'



# def decider(request):
#     if request.user.is_authenticated:
#         if request.user.is_teacher:
#             return redirect('home_views:dashboard')
#         else:
#             return redirect('index.html')
#     return render(request, 'index.html')
