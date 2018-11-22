from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def faqs(request):
    return render(request, "faqs.html")


def about(request):
    return render(request, "about.html")


def login(request):
    return render(request, "login.php")


def dashboard(request):
    return render(request, "dashboard/dashboard.php")


def pricing(request):
    return render(request, "pricing.html")


def moreinfo(request):
    return render(request, "moreinfo.php")
