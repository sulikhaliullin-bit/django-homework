from django.http import HttpResponse
from django.shortcuts import redirect

# название функции должно быть в точности show_params
def show_params(request):
    res = "введенные параметры:<br>"
    for key, value in request.GET.items():
        res += f"{key}: {value}<br>"
    return HttpResponse(res)

def buy_item(request):
    # здесь укажи имя пути на который хочешь редирект, например 'lesson_4'
    return redirect('lesson_4')