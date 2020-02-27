from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from home.decorators import client_required, owner_required
from django.http import HttpResponse, JsonResponse
import json
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.generic import TemplateView, CreateView
from home.forms import *
from home.models import Salon, Services, Owner, Products, Comments, SalonSubscription, Comments
from home.models import Client, Staff


def home(request):
    filtered_salons = Salon.objects.all().order_by('likes')
    page = request.GET.get('page', 1)
    paginator = Paginator(filtered_salons, 4)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {"salons": salons})


def signup_steps(request):

    if request.method == "POST":
        logged_in_user = request.user

        owner = Owner.objects.get(user__username=logged_in_user)

        # Processing form data
        if request.POST['input_data']:

            input_data = json.loads(request.POST['input_data'])[0]

            # Update owner details
            if 'owner_name' in input_data:
                name = input_data['owner_name']
                email = input_data['email']
                phone = input_data['phone']
                location = input_data['location']
                gender = input_data['gender']

                Owner.objects.filter(user=logged_in_user).update(
                    ownerName=name,
                    email=email,
                    phone=phone,
                    location=location,
                    gender=gender)

                results = {
                    'message_type': 'success',
                    'results': 'Account details successfully updated'
                }
                return JsonResponse(results)

            # Create new salon
            elif 'salon_name' in input_data:
                name = input_data['salon_name']
                description = input_data['description']
                paybill = input_data['paybill']
                town = input_data['town']

                if Salon.objects.filter(name=name).count() > 0:
                    results = {
                        'message_type':
                        'error',
                        'results':
                        'A salon with this name exists. Please choose another name'
                    }
                    return JsonResponse(results)

                else:
                    salon = Salon(name=name,
                                  description=description,
                                  owner=owner,
                                  paybill=paybill,
                                  town=town)
                    salon.save()

                    results = {
                        'message_type': 'success',
                        'results': 'Salon added successfully'
                    }
                    return JsonResponse(results)

            elif 'salon_name' in input_data:
                package = input_data['package']
                amount = input_data['amount']
                payment_method = input_data['payment_method']

                salon = Salon.objects.get(owner=owner)
                subscription = SalonSubscription(salon=salon,
                                                 package=package,
                                                 amount=amount,
                                                 payment_method=payment_method,
                                                 who_payed=owner)
                subscription.save()

                results = {
                    'message_type': 'success',
                    'results': 'Payment completed'
                }
                return JsonResponse(results)

        # Forms
        owner_details = OwnerAddInfoForm(request.POST)
        if owner_details.is_valid():
            salonadd = owner_details.save(commit=False)
            salonadd.save()
            return redirect('add_salon')

        add_salon = addSalonForm(request.POST)
        if add_salon.is_valid():
            salonadd = add_salon.save(commit=False)
            salonadd.save()
            return redirect('add_salon')

        salon_subsription = SalonSubscriptionForm(request.POST)
        if salon_subsription.is_valid():
            salonadd = salon_subsription.save(commit=False)
            salonadd.save()
            return redirect('add_salon')

    else:
        owner_details = OwnerAddInfoForm()
        add_salon = addSalonForm
        salon_subsription = SalonSubscriptionForm

    context = {
        'owner_details': owner_details,
        'add_salon': add_salon,
        'salon_subsription': salon_subsription
    }
    return render(request, 'sign-up-steps.html', context)


def comingsoon(request):

    if request.method == "POST":
        temuser_form = TempUserForm(request.POST)
        if temuser_form.is_valid():

            temuser = temuser_form.save(commit=False)

            temuser.save()
            messages.success(request, 'We successfully received your details!')

            return redirect('comingsoon')

    temuser_form = TempUserForm()
    return render(request, 'comingsoon/index-design-2.html',
                  {'temuserf_form': temuser_form})


def crs(request):
    people = tempuser.objects.all()
    return render(request, "comingsoon/check.html", {'people': people})


def faqs(request):
    return render(request, "faqs/index.html")


def about(request):
    return render(request, "about.html")


@login_required
@owner_required
def dashboard(request):
    salon = get_object_or_404(Salon, owner__ownerName=request.user.owner)
    if request.method == "POST":
        form = addSalonForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('dashboard')
    else:
        form = addSalonForm()

    context = {'salon': salon, 'form': form}
    print(salon.url)
    return render(request, "dashboard/dashboard.html", context)


@login_required
def profile(request, id):
    user_details = Owner.objects.get(ownerId=id)
    salon_details = Salon.objects.get(ownerId=id)
    context = {'user_details': user_details, 'salon_details': salon_details}
    return render(request, "dashboard/profile.html", context)


@login_required
def reviews(request):
    reviews = Comments.objects.all()
    context = {'reviews': reviews}
    return render(request, "dashboard/reviews.html", context)


@login_required
def services(request):
    salon = get_object_or_404(Salon, owner__ownerName=request.user.owner)
    services = Services.objects.filter(salon=salon)

    context = {'services': services, 'salon': salon}

    return render(request, "dashboard/services/index.html", context)


@login_required
def service_new(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()
    context = {'form': form}

    return render(request, "dashboard/services/new.html", context)


@login_required
def service_edit(request, id):
    service = get_object_or_404(Services, pk=id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm(instance=service)
    context = {'service': service, 'form': form}
    return render(request, "dashboard/services/edit.html", context)


@login_required
def service_delete(request, id):
    service = get_object_or_404(Services, pk=id)
    service.delete()
    return redirect('services')


def salon_details(request, name):
    salon = get_object_or_404(Salon, url=name)
    services = Services.objects.filter(salon__name=salon.name)
    products = Products.objects.filter(salons__name=salon.name)
    comments = Comments.objects.filter(
        salon__id=salon.id).order_by("-created_date")
    MAPS_API_KEY = settings.MAPS_API_KEY

    average_rating = 0
    stars_1 = 0
    stars_2 = 0
    stars_3 = 0
    stars_4 = 0
    stars_5 = 0

    ps1 = 0
    ps2 = 0
    ps3 = 0
    ps4 = 0
    ps5 = 0

    for comment in comments:
        if comment.stars == '1 Star':
            stars_1 += 1

        if comment.stars == '2 Stars':
            stars_2 += 1

        if comment.stars == '3 Stars':
            stars_3 += 1

        if comment.stars == '4 Stars':
            stars_4 += 1

        if comment.stars == '5 Stars':
            stars_5 += 1

    total_stars = stars_1 + stars_2 + stars_3 + stars_4 + stars_5
    if total_stars > 0:
        ps1 = (stars_1 / total_stars) * 100
        ps2 = (stars_2 / total_stars) * 100
        ps3 = (stars_3 / total_stars) * 100
        ps4 = (stars_4 / total_stars) * 100
        ps5 = (stars_5 / total_stars) * 100

        average_rating = 0

        average_rating = round((stars_1 + (stars_2 * 2) + (stars_3 * 3) +
                                (stars_4 * 4) + (stars_5 * 5)) / total_stars,
                               1)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            comment = comment_form.save(commit=False)
            comment.salon = salon
            comment.author = request.user

            comment.save()
            messages.success(
                request,
                'Review Received Successfully! It will be posted soon. You can edit it on your Profile'
            )
            return redirect('salon_details', name=name)

    comment_form = CommentForm()

    if request.method == "POST":
        form = clientAppointment(request.POST)
        if form.is_valid():
            clientAppointmentAdd = form.save(commit=False)
            clientAppointmentAdd.client = request.user
            clientAppointmentAdd.salons = salon
            clientAppointmentAdd.totalCost = 900
            clientAppointmentAdd.save()
            messages.success(request, 'Appointment Successfuly booked')
            return redirect('salon_details', name=name)
    form = clientAppointment()

    context = {
        'salon': salon,
        'average_rating': average_rating,
        'services': services,
        'products': products,
        'reviews': comments,
        'counter': 0,
        'comment_form': comment_form,
        'total_stars': total_stars,
        'form': form,
        'clientAppointment': clientAppointment,
        'ps1': ps1,
        'ps2': ps2,
        'ps3': ps3,
        'ps4': ps4,
        'ps5': ps5,
        'MAPS_API_KEY': MAPS_API_KEY,
        'stars_1': stars_1,
        'stars_2': stars_2,
        'stars_3': stars_3,
        'stars_4': stars_4,
        'stars_5': stars_5
    }
    return render(request, "home/salon_details.html", context)


@login_required
def services_add(request):
    context = {}
    return render(request, "dashboard/services_add.html", context)


@login_required
def products(request):
    product = Products.objects.all()

    if request.method == "POST":
        form = addProductForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('products')
    else:
        formproduct = addProductForm()

    context = {'formproduct': formproduct, 'product': product}

    return render(request, "dashboard/products.html", context)


@login_required
def products_add(request):
    context = {}
    return render(request, "dashboard/products_add.html", context)


@login_required
def customers(request):
    customers = Client.objects.all()

    if request.method == "POST":
        form = addClientForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('customers')
    else:
        formclient = addClientForm()

    context = {
        'client': customers,
        'formclient': formclient,
    }

    return render(request, "dashboard/customers.html", context)


@login_required
def staffs(request):

    staff = Staff.objects.all()

    if request.method == "POST":
        form = addEmployeeForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('staffs')
    else:
        formstaff = addEmployeeForm()

    context = {'formstaff': formstaff, 'staff': staff}

    return render(request, "dashboard/staffs.html", context)


@login_required
def staffs_add(request):
    context = {}
    return render(request, "dashboard/staffs_add.html", context)


@login_required
def dashboard_appointments_add(request):
    context = {}
    return render(request, "dashboard/appointments_add.html", context)


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
    template_name = 'dashboard/appointments.html'

    def get_queryset(self):
        data = Salon.objects.get(owner=self.request.user.owner)
        queryset = data.appointments.all()
        return queryset


def appointment_accept(
    request,
    pk,
):
    appointment = get_object_or_404(Appointments, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = False
    appointment.is_complete = False
    appointment.is_accepted = True
    appointment.save()
    return redirect('appointments', pk=pk)


def appointment_reject(
    request,
    pk,
):
    appointment = get_object_or_404(Appointments, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = True
    appointment.is_complete = False
    appointment.is_accepted = False
    appointment.save()
    return redirect('appointments', pk=pk)
