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
            return redirect('/explore_problems_codeforces')

        else:
            messages.info(request, 'invalid username or password')
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
    username = get_user(request)
    l_username = platform_details.objects.raw(
        'select Leetcode_username from all_in_one_cp_platform_details where username= %s ', [username])
    for p in l_username:
        leetcode_username = p.Leetcode_username
    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/leetcode/{leetcode_username}").json()
    return redirect(request, '/profile', {'response_leetcode': response})


def codeforces(request):
    username = get_user(request)
    c_username = platform_details.objects.raw(
        'select Codeforces_username from all_in_one_cp_platform_details where username= %s ', [username])
    for p in c_username:
        codeforces_username = p.Codeforces_username
    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/codeforces/{codeforces_username}").json()
    return redirect(request, '/profile', {'response_codeforces': response})


def SPOJ(request):
    username = get_user(request)
    s_username = platform_details.objects.raw(
        'select SPOJ_username from all_in_one_cp_platform_details where username= %s ', [username])
    for p in s_username:
        spoj_username = p.SPOJ_username
    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/spoj/{spoj_username}").json()
    return redirect(request, '/profile', {'response_spoj': response})


def interviewbit(request):
    username = get_user(request)
    i_username = platform_details.objects.raw(
        'select Interviewbit_username from all_in_one_cp_platform_details where username= %s ', [username])
    for p in i_username:
        interviewbit_username = p.Interviewbit_username
    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/interviewbit/{interviewbit_username}").json()
    return redirect(request, '/profile', {'response_interviewbit': response})


def atcoder(request):
    username = get_user(request)
    a_username = platform_details.objects.raw(
        'select Atcoder_username from all_in_one_cp_platform_details where username= %s ', [username])
    for p in a_username:
        atcoder_username = p.Atcoder_username
    response = requests.get(
        f"https://competitive-coding-api.herokuapp.com/api/atcoder/{atcoder_username}").json()
    return redirect(request, '/profile', {'response_atcoder': response})


def explore_problems(request):
    response = requests.get(
        "https://leetcode.com/api/problems/algorithms/").json()
    list1 = []
    list1.append(response)
    return render(request, 'random_problems.html', {'leetcode_problems': list1})


def explore_problems_codeforces(request):
    response = requests.get(
        "https://codeforces.com/api/problemset.problems?tags=implementation").json()
    list2 = []
    list2.append(response)
    return render(request, 'random_problems.html', {'codeforces_problems': list2})


def explore_problems_atcoder(request):
    response = requests.get(
        "https://kenkoooo.com/atcoder/resources/problems.json").json()
    list3 = []
    list3.append(response)
    return render(request, 'random_problems.html', {'atcoder_problems': list3})


def daily_coding(request):
    return render(request, 'daily_coding.html')


def problem_of_the_day(request):
    return render(request, 'problem_of_the_day.html')
