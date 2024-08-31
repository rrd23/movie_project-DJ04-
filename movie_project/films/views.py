from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Это мой Films</h1>")




# Create your views here.
