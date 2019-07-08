from django.shortcuts import render


def homepage(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about_us.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')
