from django.shortcuts import render

from .models import UserModel


def getData(request):
    score = request.POST.get('score', 0)
    UserModel.objects.filter(userName="test").update(highScore=score)
    return index(request)


def index(request):
    if not (UserModel.objects.filter(userName="test").exists()):
        UserModel.objects.create(highScore=0, userName="test")
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


def game(request):
    return render(request, '2048.html')
