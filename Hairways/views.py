from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from Hairways.models import Salons, Services
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from Hairways.filters import LocationFilter

# customer signup imports
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# customer signup function

# JAYMOHS SIGNUP ....TO BE DELETED

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')    # redirect to home and session created to allow customer to rate and comment on salons plus show message: LOGGED IN
#     else:
#         form = UserCreationForm()
#     return render(request, 'index.html', {'salons': salons})    # redirect to home but dont allow rating and commenting on salons show message: NOT LOGGED IN


def home(request):

    items = Salons.objects.all()
    # for pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 10)
    try:
        salons = paginator.page(page)
    except PageNotAnInteger:
        salons = paginator.page(1)
    except EmptyPage:
        salons = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'salons': salons})


def filterSalons(request):
    selected_location = request.GET.get()
    all_salons = Salons.objects.all()
    filtered_salons = LocationFilter(request.GET, queryset=all_salons)
    return render(request, 'index.html', {'filtered_salons': filtered_salons})


def faqs(request):
    return render(request, "faqs.html")


def about(request):
    return render(request, "about.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        "form": form})


# protecting views you can't just access dashboard without logging
@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.php")


@login_required  # protecting views
def user(request):
    return render(request, "dashboard/user.php")


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
    return render(request, "moreinfo.html", {'salon': salon})


def services(request, id):
    services = Services.objects.all(salons=id)
    return render(request, "moreinfo.html", {
        'services': services})


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
