from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from home.decorators import customer_required, vendor_required
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil import parser
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from django.views.generic import TemplateView, CreateView
from home.forms import CreateSalonForm
from home.models import Salon, Service, Gallery, Vendor, Appointment, Product, Review, MpesaTransaction
from home.models import Customer, Package
from visits.models import Visit
from home.mpesa import Mpesa
from django.views.decorators.csrf import csrf_exempt


def index(request):
    salons = Salon.objects.order_by('name').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(salons, 16)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {"salons": salons})


def faqs(request):
    return render(request, "faqs/index.html")


def about(request):
    return render(request, "about/index.html")


def transaction_progress(request):
    salon = get_object_or_404(Salon, owner=request.user.owner)
    return render(request, 'home/transactio_progress.html', {})


@csrf_exempt
def confirmation(request):
    salon = get_object_or_404(Salon, owner__name=request.user.owner)
    response = json.loads(request.body)['Body']['stkCallback']
    response_data = response['CallbackMetadata']['Item']
    response_status = response['ResultCode']
    if response_status == 0:
        raw_date = str(response_data[3]['Value'])
        date = parser.parse(str(raw_date))
        payment = MpesaTransaction(
            salon=salon,
            amount=response_data[0]['Value'],
            mpesa_receipt_number=response_data[1]['Value'],
            transaction_date=date,
            phone_number=response_data[4]['Value'],
            is_successfull=True
        )
        payment.save()
        salon.is_paid = True
        salon.save()

    elif response_status == 1:
        payment = MpesaTransaction(
            salon=salon,
            mpesa_receipt_number=response_data[1]['Value'],
            transaction_date=date,
            phone_number=response_data[4]['Value'],
            is_successfull=False
        )


def validation(request):
    return HttpResponse('validation')


def mpesa(phone_no, package_amount, package_name, salon_owner):
    mpesa = Mpesa()
    access_token = mpesa.get_access_token()
    mpesa.register_url(access_token)
    timestamp = mpesa.timestamp()
    password = mpesa.lipa_na_mpesa_password(timestamp)
    mpesa.lipa_na_mpesa_online(
        access_token, password, timestamp, phone_no, package_amount, package_name, salon_owner)


def signup_steps(request):

    if request.method == "POST":

        logged_in_user = request.user

        owner = Vendor.objects.get(user__username=logged_in_user)

        # Processing form data
        if 'input_data' in request.POST:

            input_data = json.loads(request.POST['input_data'])[0]

            # Update owner details
            if 'owner_name' in input_data:
                name = input_data['owner_name']
                email = input_data['email']
                phone = input_data['phone']
                location = input_data['location']

                Vendor.objects.filter(user=logged_in_user).update(
                    name=name,
                    email=email,
                    phone=phone,
                    location=location
                )

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

        elif 'phone_no' in request.POST:
            phone_no = '254'+request.POST['phone_no'][-9:]
            package_amount = request.POST['package_amount']
            package_name = request.POST['package_name']
            salon_owner = str(request.user)

            mpesa(phone_no, package_amount, package_name, salon_owner)

            return redirect('transaction_progress')

        # Forms
        owner_details = VendorAddInfoForm(request.POST)
        if owner_details.is_valid():
            salonadd = owner_details.save(commit=False)
            salonadd.save()
            return redirect('new_salon')

        add_salon = CreateSalonForm(request.POST)
        if add_salon.is_valid():
            salonadd = add_salon.save(commit=False)
            salonadd.save()
            return redirect('new_salon')

    else:
        owner_details = VendorAddInfoForm()
        add_salon = CreateSalonForm
        packages = Package.objects.all()
        package_details = PackageDetail.objects.all()

        context = {
            'packages': packages,
            'owner_details': owner_details,
            'add_salon': add_salon,
            'package_details': package_details
        }
        return render(request, 'sign-up-steps.html', context)


def client_profile_for_salons(request, pk):
    client = get_object_or_404(Customer, pk=pk)
    bookings = (Appointment.objects.filter(client=client.pk)).count()
    return render(request, 'customer/about.html', {
        'client': client,
        'bookings': bookings
    })


"""
Takes date and returns a string of the day of the week
"""


def day_of_week(date):
    return date.strftime('%A')[:3].lower()


"""
Takes date and returns a string of the month of the year
"""


def month_of_year(date):
    return date.strftime('%B')[:3].lower()


""" Returns string of all previous 12 month names"""


def months_of_year():
    count = 0
    months = []
    while count < 12:
        date = datetime.now() - relativedelta(months=count)
        month = date.strftime('%B')[:3]
        count += 1

        months.append(month)

    return months[::-1]


monthly_chart_datas = []


@login_required
@vendor_required
def dashboard(request):
    salon = get_object_or_404(Salon, owner__name=request.user.owner)
    visits = Visit.objects.get_uri_visits_for(request, uri=salon.slug)
    end_date = datetime.date(datetime.now())
    start_date = end_date - timedelta(days=7)
    end_month = datetime.date(datetime.now())
    start_month = end_month - relativedelta(months=12)
    weekly_appointments = Appointment.objects.filter(
        salon=salon,
        created_date__range=(start_date,
                             end_date)).order_by('created_date').all()
    monthly_appointments = Appointment.objects.filter(
        salon=salon,
        created_date__range=(start_month,
                             end_month)).order_by('created_date').all()

    weekly_chart_data = {
        'mon': 0,
        'tue': 0,
        'wed': 0,
        'thu': 0,
        'fri': 0,
        'sat': 0,
        'sun': 0
    }
    monthly_chart_data = {
        'jan': 0,
        'feb': 0,
        'mar': 0,
        'apr': 0,
        'may': 0,
        'jun': 0,
        'jul': 0,
        'aug': 0,
        'sep': 0,
        'oct': 0,
        'nov': 0,
        'dec': 0,
    }
    for appointment in weekly_appointments:
        weekly_chart_data[day_of_week(
            appointment.created_date)] = weekly_appointments.filter(
                created_date=appointment.created_date).count()
    weekly_chart_data = [
        weekly_chart_data['mon'], weekly_chart_data['tue'],
        weekly_chart_data['wed'], weekly_chart_data['thu'],
        weekly_chart_data['fri'], weekly_chart_data['sat'],
        weekly_chart_data['sun']
    ]
    monthly_appointments_data = []
    for appointment in monthly_appointments:
        monthly_chart_data[month_of_year(
            appointment.created_date)] = monthly_appointments.filter(
                created_date=appointment.created_date).count()

        for month in months_of_year():
            monthly_appointments_data.append(monthly_chart_data[month.lower()])

    appointments = Appointment.objects.filter(salon__owner=request.user.owner)
    context = {
        'salon': salon,
        'months_of_year': months_of_year(),
        'weekly_chart_data': weekly_chart_data,
        'monthly_appointments_data': monthly_appointments_data,
        'appointments': appointments
    }
    return render(request, "dashboard/dashboard.html", context)


@login_required
def profile(request, id):
    user_details = Vendor.objects.get(ownerId=id)
    salon_details = Salon.objects.get(ownerId=id)
    context = {'user_details': user_details, 'salon_details': salon_details}
    return render(request, "dashboard/profile.html", context)


@login_required
def reviews(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, "dashboard/reviews.html", context)


"""
 Service CRUD
 """


@login_required
def services(request):
    salon = get_object_or_404(Salon, owner__name=request.user.owner)
    services = Service.objects.filter(salon=salon)

    context = {'services': services, 'salon': salon}

    return render(request, "dashboard/services/index.html", context)


@login_required
def service_new(request):
    if request.method == "POST":
        salon = get_object_or_404(Salon, owner=request.user.owner.pk)
        form = ServiceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.salon = salon
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()
    context = {'form': form}

    return render(request, "dashboard/services/new.html", context)


@login_required
def service_edit(request, id):
    service = get_object_or_404(Service, pk=id)
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
    service = get_object_or_404(Service, pk=id)
    service.delete()
    return redirect('services')


"""
 Product CRUD
"""


@login_required
def products(request):
    salon = get_object_or_404(Salon, owner__name=request.user.owner)
    products = Product.objects.filter(salon=salon)

    context = {'products': products, 'salon': salon}

    return render(request, "dashboard/products/index.html", context)


@login_required
def product_new(request):
    if request.method == "POST":
        salon = get_object_or_404(Salon, owner=request.user.owner.pk)
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.salon = salon
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    context = {'form': form}

    return render(request, "dashboard/products/new.html", context)


@login_required
def product_edit(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    context = {'product': product, 'form': form}
    return render(request, "dashboard/products/edit.html", context)


@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('products')


@login_required
def customers(request):
    customers = Customer.objects.all()

    if request.method == "POST":
        form = addCustomerForm(request.POST)
        if form.is_valid():
            salonadd = form.save(commit=False)
            salonadd.save()
            return redirect('customers')
    else:
        formclient = addCustomerForm()

    context = {
        'client': customers,
        'formclient': formclient,
    }

    return render(request, "dashboard/customers.html", context)


@login_required
def dashboard_appointments_new(request):
    context = {}
    return render(request, "dashboard/appointments/new.html", context)


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


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def appointments(request):
    my_salon = Appointment.objects.filter(salon__owner=request.user.owner)
    salon = get_object_or_404(Salon, owner=request.user.owner.pk)
    services = Service.objects.filter(salon__name=salon.name)
    products = Product.objects.filter(salon__name=salon.name)
    if request.method == "POST":
        form = clientAppointment(request.POST)
        if form.is_valid():
            clientAppointmentAdd = form.save(commit=False)
            clientAppointmentAdd.client = request.user
            clientAppointmentAdd.salon = salon
            clientAppointmentAdd.totalCost = 900
            clientAppointmentAdd.save()
            form.save_m2m()
            messages.success(request, 'Appointment Successfuly booked')
            return redirect('dashboard_appointments')
    form = clientAppointment()
    context = {
        'services': services,
        'products': products,
        'form': form,
        'my_salon': my_salon,
    }

    return render(request, 'dashboard/appointments/index.html', context)


def appointment_accept(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = False
    appointment.is_complete = False
    appointment.is_accepted = True
    appointment.save()
    return redirect('appointments', pk=pk)


def appointment_complete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'Completed'
    appointment.save()
    return redirect('dashboard_appointments', )


def appointment_reject(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.is_pending = False
    appointment.is_rejected = True
    appointment.is_complete = False
    appointment.is_accepted = False
    appointment.save()
    return redirect('appointments', pk=pk)


def salon_images(request, slug):
    salon = get_object_or_404(Salon, slug=slug)
    images = Gallery.objects.filter(salon=salon)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            imageAdd = form.save(commit=False)
            imageAdd.salon = salon
            imageAdd.save()
            messages.success(request, 'Imabge succesfully added')
            return redirect('salon_images', request.user.owner.my_salons.slug)
    form = ImageForm()

    context = {
        'images': images,
        'form': form
    }

    return render(request, 'dashboard/salon_images/index.html', context)


def select_image(request, slug, id):
    salon = get_object_or_404(Salon, slug=slug)
    images = Gallery.objects.filter(salon=salon)
    img = get_object_or_404(Gallery, id=id)
    if img.image_position == "Card Image":
        current_card_image = images.filter(
            image_position="Card Image")
        for image in current_card_image:
            if image.id == id:
                image.is_selected = True
                image.save()
                salon.card_img = image.image.url
                salon.save()

            else:
                image.is_selected = False
                image.save()

    elif img.image_position == "Cover Image":
        cover_image = images.filter(
            image_position="Cover Image")
        for image in cover_image:
            if image.id == id:
                image.is_selected = True
                image.save()
                salon.cover_img = image.image.url
                salon.save()
            else:
                image.is_selected = False
                image.save()
    else:
        cover_image = images.filter(
            image_position="Prome Image")
        for image in cover_image:
            if image.id == id:
                image.is_selected = True
                image.save()
                salon.promo_img = image.url
                salon.save
            else:
                image.is_selected = False
                image.save()

    return redirect('salon_images', request.user.owner.my_salons.slug)


def user_profile(request):
    owner_to_update = get_object_or_404(Vendor, pk=request.user.id)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=owner_to_update)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileUpdateForm(instance=owner_to_update)

    if request.method == "POST":
        ppicform = PpicUpdateForm(
            request.POST, request.FILES, instance=request.user)
        if ppicform.is_valid():
            ppicform.save()
            return redirect('user_profile')
    else:
        ppicform = PpicUpdateForm(instance=request.user)

    context = {
        'form': form, 'ppicform': ppicform}

    return render(request, 'dashboard/user_profile/index.html', context)
