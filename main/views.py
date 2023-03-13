from django.shortcuts import render

# Create your views here.


# New Pages for the Admin Dashboard


def home(request):
    return render(request, "html/index.html")

def reportsMain(request):
    return render(request, "html/pages/main/analytics.html")

# For Emailer Views
def emailer(request):
    return render(request, "html/emailer.html")

def emailerView(request):
    return render(request, "html/emailer-viewed.html")

# For Authrization Views
def login(request):
    return render(request, "html/login.html")
