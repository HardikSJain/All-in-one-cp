from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from all_in_one_cp import views
urlpatterns = [

    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.register, name="register"),
    path('profile', views.profile, name="profile"),
    path('leetcode', views.leetcode, name="leetocde_stats"),
    path('codeforces', views.codeforces, name="codeforces_stats"),
    path('SPOJ', views.SPOJ, name="spoj_stats"),
    path('interviewbit', views.interviewbit, name="interviewbit_stats"),
    path('atcoder', views.atcoder, name="atcoder_stats"),
    path('explore_problems', views.explore_problems, name="problems"),
    path('daily_coding', views.daily_coding, name="daily_coding"),
    path('problem_of_the_day', views.problem_of_the_day, name="probken_of_the_day"),

]
