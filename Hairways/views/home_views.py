from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from Hairways.models import Salons, Services, Owners, Products, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..decorators import client_required
from ..decorators import owner_required
from django.http import HttpResponse
import json
from django.core import serializers
from django.views.generic import TemplateView

from django.views.generic import CreateView

from ..forms import CommentForm

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


def pricing(request):
    return render(request, "pricing.html")


def moreinfo(request, id):
    salon = Salons.objects.get(id=id)
    services = Services.objects.all()
    products = Products.objects.all()
    reviews = Comments.objects.filter(salon__id=id)

# Comments form
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            print('valid')

            comment = form.save()
            comment.author = request.user.username

            comment.save()

            return redirect('moreinfo', id=salon.id)

    form = CommentForm()
    return render(request, "moreinfo.html", {'salon': salon, 'services' : services, 'products' : products, 'reviews' : reviews, 'counter': 0, 'form': form})

def salonLike(request):
    salon = get_object_or_404(Client, id=request.POST.get('salon_id'))
    print(salon_id)
    salon.likes.add(request.client)
    return HttpResponseRedirect(post.get_absolute_url())


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html', context)
    context['url'] = fs.url(name)


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

#       METHOD FOR COMMENT FORM to be reviewed and discarded
# def moreinfo(request, id):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             print('valid')
#
#             comm = form.save()
#             comm.salon = request.salon
#             comm.save()
#             return redirect('moreinfo')
#
#     form = CommentForm()
#     return render(request, 'moreinfo.html', {'form': form})


# def decider(request):
#     if request.user.is_authenticated:
#         if request.user.is_teacher:
#             return redirect('home_views:dashboard')
#         else:
#             return redirect('index.html')
#     return render(request, 'index.html')
