from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from home.decorators import client_required, owner_required
from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.generic import TemplateView, CreateView
from home.forms import *
from home.models import Salon, Services, Owner, Products, Comments
from home.models import Client, Staff


def home(request):
    filtered_salons = Salon.objects.all().order_by('likes')
    page = request.GET.get('page', 1)
    paginator = Paginator(filtered_salons, 10)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)

    return render(request, 'home/index.html', {"salons": salons})


def faqs(request):
    return render(request, "faqs/index.html")


def about(request):
    return render(request, "about.html")


@method_decorator([login_required, owner_required], name='dispatch')
def dashboard(request):
    me = Salon.objects.all()
    if request.method == "POST":
        form = addSalonForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('dashboard')
    else:
        form = addSalonForm()

    context = {'me': me, 'form': form}
    return render(request, "dashboard/dashboard.html", context)


@login_required
def user(request, id):
    user_details = Owner.objects.get(ownerId=id)
    salon_details = Salon.objects.get(ownerId=id)
    context = {'user_details': user_details, 'salon_details': salon_details}
    return render(request, "dashboard/user.html", context)


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

    context = {'formservice': formservice, 'formproduct': formproduct,
               'service': service, 'product': product}
    return render(request, "dashboard/productsServices.php", context)


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

    context = {'formstaff': formstaff, 'formclient': formclient,
               'client': client, 'staff': staff}
    return render(request, "dashboard/staffClients.php", context)


@login_required
def map(request):
    return render(request, "dashboard/map.php")


@login_required
def calendar(request):
    return render(request, "dashboard/calendar.php")


@login_required
def upgrade(request):
    return render(request, "dashboard/upgrade.php")


def moreinfo(request, name):
    salon = get_object_or_404(Salon, url=name)
    services = Services.objects.filter(salons__name=salon.name)
    products = Products.objects.filter(salons__name=salon.name)
    comments = Comments.objects.filter(
        salon__id=salon.id).order_by("-created_date")

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            comment = comment_form.save(commit=False)
            comment.salon = salon
            comment.author = request.user

            comment.save()

            return redirect('moreinfo', name=name)

    comment_form = CommentForm()

    if request.method == "POST":
        form = clientAppointment(request.POST)
        if form.is_valid():
            clientAppointmentAdd = form.save(commit=False)
            clientAppointmentAdd.save()
            return redirect('moreinfo', name=name)
    form = clientAppointment()
    context = {'salon': salon, 'services': services, 'products': products,
               'reviews': comments, 'counter': 0, "comment_form": comment_form,
               'form': form, 'clientAppointment': clientAppointment}
    return render(request, "home/show.html", context)


def sort_comments():
    pass


@login_required
def preference(request):
    if request.method == "POST":
        salon_id = request.POST.get('salon_id', None)
        salon = get_object_or_404(Salon, id=salon_id)
        user = request.user

        if salon.likes.filter(id=user.id):
            # User has already liked this salon
            # remove this user like
            salon.likes.remove(user)
            message = "dislike"
        else:
            # user likes salon
            salon.likes.add(user)
            message = "like"
        context = {"likes_count": salon.total_likes, "message": message}
    return HttpResponse(json.dumps(context), content_type='application/json')


def clientPayment(request):
    return render(request, "payment.html")


@csrf_exempt
def visits(request):
    if request.method == 'POST' and request.is_ajax():
        get_view = request.POST.get('salonId', False)
        update_view = Salon.objects.get(id=get_view)
        update_view.views += 1
        update_view.save()
        message = "Salon With ID %s Views Was \
                Updated successfully" % update_view.views
    return HttpResponse(message)


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


@method_decorator([login_required, owner_required], name='dispatch')
class AppointmentListView(generic.ListView):
    model = Salon
    context_object_name = 'my_salon'
    template_name = 'dashboard/dashboard.html'

    def get_queryset(self):
        data = Salon.objects.get(Owner=self.request.user.owner)
        queryset = data.appointments.all()
        return queryset


def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointments, pk=pk)
    context = {'appointment': appointment}
    return render(request, 'dashboard/appointment_detail.html', context)


def appointment_accept(request, pk,):
    appointment = get_object_or_404(Appointments, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = False
    appointment.is_complete = False
    appointment.is_accepted = True
    appointment.save()
    return redirect('appointment_detail', pk=pk)


def appointment_reject(request, pk,):
    appointment = get_object_or_404(Appointments, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = True
    appointment.is_complete = False
    appointment.is_accepted = False
    appointment.save()
    return redirect('appointment_detail', pk=pk)
