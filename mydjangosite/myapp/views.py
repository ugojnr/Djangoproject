from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myapp/index.html", {})


def shop(request):
    return render(request, "myapp/shop.html", {})



