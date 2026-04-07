from django.http import HttpResponse, JsonResponse

def hello_world(request):
    return HttpResponse("<h1>Привет!</h1><p>Это строка с HTML тегами для практической работы.</p>")

def get_data(request):
    data = [x for x in range(1, 11)]
    return JsonResponse(data, safe=False)