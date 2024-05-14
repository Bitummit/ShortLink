from .models import Link
from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_short(request, short_link):
    try:
        link = Link.objects.filter(short_link=short_link).values("full_link").first()
        return redirect(link["full_link"])
    except Exception as e:
        return HttpResponse(e.args)