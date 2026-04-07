from django.http import HttpResponse, JsonResponse
from .models import Bb

def hello_world(request):
    return HttpResponse("<h1>Привет!</h1><p>Это строка с HTML тегами.</p>")

def get_data(request):
    data = [x for x in range(1, 11)]
    return JsonResponse(data, safe=False)

def filter_data(request):

    results = Bb.objects.values('title', 'price').exclude(price__isnull=True).exclude(price=0)
    return JsonResponse(list(results), safe=False)