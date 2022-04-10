from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from all_in_one_cp.models import user_details, platform_details
from django.contrib import messages
from django.contrib.auth import authenticate, get_user, login, logout
import requests


def home(request):
    return render(request, 'home.html')


def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully as '+username)
            return redirect('/explore_problems')

        else:
            messages.warning(request, 'invalid username or password')
            return redirect("/login")
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        leetcode = request.POST.get("leetcode")
        codeforces = request.POST.get("codeforces")
        spoj = request.POST.get("spoj")
        interviewbit = request.POST.get("interviewbit")
        atcoder = request.POST.get("atcoder")
        password = request.POST.get("password")
        cpassword = request.POST.get("confirmpassword")

        if(len(username) <= 25 and password == cpassword):
            user = User.objects.create_user(
                first_name=name, username=username, password=password)
            userdata = user_details(
                name=name, username=username, password=password, email=email)
            platform_usernames = platform_details(username=username, Leetcode_username=leetcode, Codeforces_username=codeforces,
                                                  SPOJ_username=spoj, Interviewbit_username=interviewbit, Atcoder_username=atcoder)

            user.save()
            userdata.save()
            platform_usernames.save()
            messages.success(
                request, 'Your account is created successfully with username: '+username)
            return redirect("/login")
        elif len(username) > 25:
            messages.warning(
                request, 'Username Length Should be less than 25!')
            return redirect("/login")
        elif password != cpassword:
            messages.warning(
                request, 'Entered Password do not match')
            return redirect('/login'+'#signup')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged out Successfully ')
    return redirect("/")


def profile(request):
    return render(request, 'profile.html')


def leetcode(request):
    leetcode_username = request.POST.get("username_leetcode")

    response = requests.get(
        f'https://competitive-coding-api.herokuapp.com/api/leetcode/{leetcode_username}').json()
    list1 = []
    list1.append(response)
    print(list1)
    return render(request, 'profile.html', {'response_leetcode': list1})


def codeforces(request):
    codeforces_username = request.POST.get("username_codeforces")
    print(codeforces_username)

    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/codeforces/{codeforces_username}").json()
    list1 = []
    list1.append(response)
    print(list1)
    return render(request, 'profile.html', {'response_codeforces': list1})


def SPOJ(request):
    spoj_username = request.POST.get("username_spoj")

    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/spoj/{spoj_username}").json()
    list1 = []
    list1.append(response)
    print(list1)
    return render(request, 'profile.html', {'response_spoj': list1})


def atcoder(request):
    atcoder_username = request.POST.get("username_atcoder")

    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/atcoder/{atcoder_username}").json()
    list1 = []
    list1.append(response)
    print(list1)
    return render(request, 'profile.html', {'response_atcoder': list1})


def explore_problems(request):
    responsedata = requests.get(
        "https://leetcode.com/api/problems/algorithms/").json()

    response1 = requests.get(
        "https://codeforces.com/api/problemset.problems?tags=implementation").json()
    list2 = []
    list2.append(response1)

    response2 = requests.get(
        "https://kenkoooo.com/atcoder/resources/problems.json").json()

    return render(request, 'random_problems.html', {'responsedata': responsedata, 'codeforces_problems': list2, 'atcoder_problems': response2})


def daily_coding(request):
    return render(request, 'daily_coding.html')


def problem_of_the_day(request):
    return render(request, 'problem_of_the_day.html')
