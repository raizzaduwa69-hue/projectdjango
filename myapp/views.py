import requests
from django.shortcuts import render

def home(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    context = {
        "posts": data
    }

    return render(request, 'App/home.html', context)


def about(request):
    return render(request, 'App/about.html')


def contact(request):
    return render(request, 'App/contact.html')
