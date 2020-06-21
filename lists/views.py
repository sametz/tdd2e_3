from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    """

    Args:
        request: django.http.HttpRequest

    Returns:
        django.shortcuts.render

    """
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
