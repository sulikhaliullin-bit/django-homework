import logging
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

def show_params(request):
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    logging.info(f"method: {request.method}, path: {request.path}")

    res = "введенные параметры:<br>"
    for key, value in request.GET.items():
        res += f"{key}: {value}<br>"
    return HttpResponse(res)

def buy_item(request):
    if not request.user.is_authenticated:
        return redirect(reverse('index'))
    return redirect(reverse('index'))