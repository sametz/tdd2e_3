from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.utils.html import escape

from lists.models import Item, List


def home_page(request):
    """
    Args:
        request: django.http.HttpRequest

    Returns:
        django.shortcuts.render

    """
    return render(request, 'home.html')


def view_list(request, list_id=None):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = escape("You can't have an empty list item")
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{list_.id}/')


# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')
