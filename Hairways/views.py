from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from Hairways.forms import SignUpForm


def home(request):
    return render(request, "index.html")


def faqs(request):
    return render(request, "faqs.html")


def about(request):
    return render(request, "about.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    return render(request, "dashboard/dashboard.php")

def user(request):
    return render(request, "dashboard/user.php")

def productsServices(request):
    return render(request, "dashboard/productsServices.php")

def staffClients(request):
    return render(request, "dashboard/staffClients.php")

def map(request):
    return render(request, "dashboard/map.php")

def calendar(request):
    return render(request, "dashboard/calendar.php")

def upgrade(request):
    return render(request, "dashboard/upgrade.php")

def pricing(request):
    return render(request, "pricing.html")

def moreinfo(request):
    return render(request, "moreinfo.php")
