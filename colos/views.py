from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def pricing(request):
    return render(request, 'pricing.html')


def schedule(request):
    return render(request, 'schedule.html')


def single_post(request):
    return render(request, 'single-post.html')


def speakers(request):
    return render(request, 'speakers.html')


def sponsors(request):
    return render(request, 'sponsors.html')
