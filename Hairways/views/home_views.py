from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from Hairways.models import Salons, Services, Owner, Products, Comments, Client, Staff
from Hairways.models import Salons, Likes, Services, Owner, Products, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..decorators import client_required
from ..decorators import owner_required
from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.generic import TemplateView

from django.views.generic import CreateView

from ..forms import *

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



# protecting views you can't just access dashboard without logging
@method_decorator([login_required, owner_required], name='dispatch')
def dashboard(request):
    me = Salons.objects.all()
    if request.method == "POST":
        form = addSalonForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('dashboard')
    else:
        form = addSalonForm()

    return render(request, "dashboard/dashboard.html", {'me': me, 'form': form})


@login_required  # protecting views
def user(request, id):
    user_details = Owner.objects.get(ownerId=id)
    salon_details = Salons.objects.get(ownerId=id)
    return render(request, "dashboard/user.html", {'user_details': user_details, 'salon_details' : salon_details})


@login_required
def productsServices(request):
    service = Services.objects.all()
    product = Products.objects.all()

    print(service, product)

    if request.method == "POST":
        form = addServiceForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('productsServices')
    else:
        formservice = addServiceForm()

    if request.method == "POST":
        form = addProductForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('productsServices')
    else:
        formproduct = addProductForm()

    return render(request, "dashboard/productsServices.php", {'formservice': formservice, 'formproduct' : formproduct, 'service' : service, 'product' : product})


@login_required
def staffClients(request):
    client = Client.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        form = addEmployeeForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('staffClients')
    else:
        formstaff = addEmployeeForm()

    if request.method == "POST":
        form = addClientForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('dashboard')
    else:
        formclient = addClientForm()

    return render(request, "dashboard/staffClients.php", {'formstaff': formstaff, 'formclient' : formclient, 'client' : client, 'staff' : staff})


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
    salon = Salons.objects.get(id=id) # moving to Salons model, and getting salonNameand then filtering it
    services = Services.objects.filter(salons__salonName=salon.salonName)
    products = Products.objects.filter(salons__salonName=salon.salonName)
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

@csrf_exempt
def update_views(request):
    if request.method == 'POST' and request.is_ajax():
        get_view = request.POST.get('salonId', False)
        update_view = Salons.objects.get(id=get_view)
        update_view.views +=1
        update_view.save()
    return HttpResponse("Salon With ID %s Views Was Updated successfully" % update_view.views)


def likedSalon(request):
    if request.method == 'GET':
        salon_id = request.GET['salon_id']
        # likedSalon = Salons.objects.get(pk=salon_id) # Getting the liked post
        # m = Salons(salon=likedSalon) # Creating Like Object
        # m.save() #saving it to store in database
        # return HttpResponse("Success!") # Sending an success response
    else:
        return HttpResponse("request method is not GET")


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



from django.views import generic

@method_decorator([login_required, owner_required], name='dispatch')
class AppointmentListView(generic.ListView):
    model = Salons
    context_object_name = 'my_salon'
    template_name = 'dashboard/dashboard.html'

    def get_queryset(self):
        data = Salons.objects.get(Owner = self.request.user.owner)
        queryset = data.appointments.all()
        return queryset


def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointments, pk=pk)
    return render(request, 'dashboard/appointment_detail.html', {'appointment': appointment})


def appointment_accept(request, pk ,):
    appointment = get_object_or_404(Appointments, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = False
    appointment.is_complete = False
    appointment.is_accepted = True
    appointment.save()
    # ticket.mark_closed(closer)
    return redirect('appointment_detail', pk=pk)

def appointment_reject(request, pk ,):
    appointment = get_object_or_404(Appointments, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = True
    appointment.is_complete = False
    appointment.is_accepted = False
    appointment.save()
    # ticket.mark_closed(closer)
    return redirect('appointment_detail', pk=pk)
