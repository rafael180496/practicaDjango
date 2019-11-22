from django.shortcuts import render
from .models import Page
# Create your views here.


def page(request, page_id, page_slug):
    try:
        page = Page.objects.get(id=page_id)
        
    except Exception:
        return render(request, 'core/error.html', {'err': 404})

    return render(request, 'pages/sample.html', {'page': page})