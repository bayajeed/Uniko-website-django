from django.shortcuts import render

def home_view(request):
    return render(request, 'Pages/home.html')

def about_view(request):
    return render(request, 'Pages/about.html')

def services_view(request):
    return render(request, 'Pages/services.html')

def portfolio_view(request):
    return render(request, 'Pages/portfolio.html')
