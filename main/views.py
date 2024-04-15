from django.http import HttpResponse
from django.shortcuts import render


def index(reguest):
    return render(reguest,'main/Главная.html')
def contacts_view(reguest):
    return render(reguest,'main/Контакты.html')
def about_view(reguest):
    return render(reguest,'main/О-нас.html')
def ours_view(reguest):
    return render(reguest,'main/Наши-специалисты.html')