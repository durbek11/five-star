from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def home(request):
    rate = RateStar.objects.filter(score=2).order_by("?").first()
    context = {
        "rate": rate
    }
    return render(request, "home.html", context )

def rate_img(request):
    if request.method == "POST":
        el_vd = request.POST.get("el_vd")
        rate = RateStars.objects.get(id=el_vd)
        rate.score = val
        rate.save()
        return JsonResponse({"success": "true", "score": val}, safe=False)
    return JsonResponse({"success": "false"})
