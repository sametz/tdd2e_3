# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    """

    Args:
        request: django.http.HttpRequest

    Returns:
        django.shortcuts.render

    """
    return render(request, 'home.html')
