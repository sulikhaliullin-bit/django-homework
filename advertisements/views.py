from django.http import HttpResponse
from django.shortcuts import redirect


def show_params(request):
    res = "введенные параметры:<br>"
    for key, value in request.GET.items():
        res += f"{key}: {value}<br>"
    return HttpResponse(res)

def buy_item(request):

    return redirect('lesson_4')