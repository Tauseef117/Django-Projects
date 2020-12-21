from django.http import HttpResponse

# Create your views here.

def index2(request):
    return HttpResponse("Hello World!")

def products(request):
    return HttpResponse("Products")