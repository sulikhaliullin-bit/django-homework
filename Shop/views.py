from django.http import JsonResponse

def get_data(request):
    data = [i for i in range(1, 11)]
    return JsonResponse(data, safe=False)