from django.shortcuts import render

# Create your views here.


def home_page(request):
    """

    Args:
        request: django.http.HttpRequest

    Returns:
        django.shortcuts.render

    """
    return render(request, 'home.html', {
        # in order for a 'get' request to pass the test for using the template,
        # an empty string is needed to be used for the initial page.
        # Using the .get method allows a default to be returned.
        'new_item_text': request.POST.get('item_text', '')
    })
