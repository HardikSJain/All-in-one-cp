from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def profile(request):
    return render(request, 'profile.html')


def explore_problems(request):
    return render(request, 'random_problems.html')


def daily_coding(request):
    return render(request, 'daily_coding.html')


def problem_of_the_day(request):
    return render(request, 'problem_of_the_day.html')
