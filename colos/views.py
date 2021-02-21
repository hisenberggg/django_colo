from django.shortcuts import render

from .models import UserModel
import mux_python
from mux_python.rest import ApiException

def getData(request):
    if request.user.is_authenticated and UserModel.objects.filter(userName=request.user.username).exists():
        score = request.POST.get('score', 0)
        UserModel.objects.filter(userName=request.user.username).update(highScore=score)
    return about(request)


def index(request):
    if request.user.is_authenticated and not UserModel.objects.filter(userName=request.user.username).exists():
        UserModel.objects.create(highScore=0, userName=request.user.username)
    # if not (UserModel.objects.filter(userName="test").exists()):
    #    UserModel.objects.create(highScore=0, userName="test")

    configuration = mux_python.Configuration()

    configuration.username = "524cd69c-a31b-4d52-ad6b-8105e8352e83"
    configuration.password = "3wwTGCf+U9PGT8rMHW95Lx7VvZEUMkFMtJ/KbW7BsZ5rEc3cA9KDLq9iE4mbcNaxDS5VpNhmIwL"
    assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))


    '''print("Listing Assets: \n")
    try:
        list_assets_response = assets_api.list_assets()
        for asset in list_assets_response.data:
            print('Asset ID: ' + asset.id)
            print('Status: ' + asset.status)
            print('Duration: ' + str(asset.duration) + "\n")
    except ApiException as e:
        print("Exception when calling AssetsApi->list_assets: %s\n" % e)'''
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
    i = UserModel.objects.all().count()
    userData = []

    if i>0:
        for m in range(0, i):
            userData.append(UserModel.objects.all()[m])

    print(len(userData))

    context = {
        'userData': userData,
    }
    return render(request, '2048.html', context)
