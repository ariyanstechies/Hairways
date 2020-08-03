from django.views.generic import (CreateView, DetailView)
from home.models import Salon, Service, Product, Review
from home.decorators import vendor_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from visits.models import Visit
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from home.forms import ReviewForm, CustomerAppointmentForm


@method_decorator([login_required, vendor_required], name='dispatch')
class SalonCreateView(CreateView):
    model = Salon
    fields = ('name', 'description', 'paybill', 'location')
    template_name = 'owners/salon_add_form.html'

    def form_valid(self, form):
        salon = form.save(commit=False)
        salon.vendor = self.request.user.owner
        salon.url = slugify(salon.name)
        salon.save()
        messages.success(self.request, 'The Salon was created succesfully.')
        return redirect('dashboard_appointments')


def salon_details(request, name):
    # TODO refactor this method and convert it to cbv
    # Page we are listening for unique urls visits
    Visit.objects.add_uri_visit(request, request.META["PATH_INFO"], 'home')
    salon = get_object_or_404(Salon, slug=name)
    services = Service.objects.filter(salon__name=salon.name)
    products = Product.objects.filter(salon__name=salon.name)
    reviews = Review.objects.filter(
        salon__id=salon.id).order_by("-created_date")
    MAPS_API_KEY = settings.MAPS_API_KEY

    average_rating = 0.0
    stars_1 = stars_2 = stars_3 = stars_4 = stars_5 = 0
    ps1 = ps2 = ps3 = ps4 = ps5 = 0

    for review in reviews:
        if review.stars == '1 Star':
            stars_1 += 1

        if review.stars == '2 Stars':
            stars_2 += 1

        if review.stars == '3 Stars':
            stars_3 += 1

        if review.stars == '4 Stars':
            stars_4 += 1

        if review.stars == '5 Stars':
            stars_5 += 1

    total_stars = stars_1 + stars_2 + stars_3 + stars_4 + stars_5
    if total_stars > 0:
        ps1 = (stars_1 / total_stars) * 100
        ps2 = (stars_2 / total_stars) * 100
        ps3 = (stars_3 / total_stars) * 100
        ps4 = (stars_4 / total_stars) * 100
        ps5 = (stars_5 / total_stars) * 100
        average_rating = round((stars_1 + (stars_2 * 2) + (stars_3 * 3) +
                                (stars_4 * 4) + (stars_5 * 5)) / total_stars,
                               1)
        salon.rating = average_rating
        salon.save()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        data = request.POST.copy()
        if form.is_valid():
            form = form.save(commit=False)
            form.salon = salon
            form.author = request.user
            form.ambience_rating = data.get('ambience', 0.0)
            form.cleanliness_rating = data.get('cleanliness', 0.0)

            form.save()
            messages.success(
                request,
                'Review Received Successfully! It will be posted soon. You can edit it on your Profile'
            )
            return redirect('show_salon', name=name)
    else:
        review_form = ReviewForm()

    if request.method == "POST":
        form = CustomerAppointmentForm(request.POST)
        if form.is_valid():
            clientAppointmentAdd = form.save(commit=False)
            clientAppointmentAdd.client = request.user
            clientAppointmentAdd.salon = salon
            clientAppointmentAdd.totalCost = 900
            clientAppointmentAdd.save()
            messages.success(request, 'Appointment Successfuly booked')
            return redirect('show_salon', name=name)
    form = CustomerAppointmentForm()

    context = {
        'salon': salon,
        'average_rating': average_rating,
        'services': services,
        'products': products,
        'reviews': reviews,
        'counter': 0,
        'review_form': review_form,
        'total_stars': total_stars,
        'form': form,
        'clientAppointment': CustomerAppointmentForm,
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
    return render(request, "salon/details.html", context)
