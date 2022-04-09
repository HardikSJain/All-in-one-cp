from django.db import models
from sqlalchemy import false, true

# Create your models here.


class user_details(models.Model):
    name = models.CharField(max_length=200, null=False, unique=False)
    username = models.CharField(
        max_length=200, null=False, unique=True, primary_key=True)
    password = models.CharField(max_length=200, null=False, unique=True)


class platform_details(models.Model):
    username = models.CharField(
        max_length=200, null=False, unique=True, primary_key=True)
    Leetcode_username = models.CharField(
        max_length=200, null=False, unique=False)
    Codeforces_username = models.CharField(
        max_length=200, null=False, unique=False)
    SPOJ_username = models.CharField(
        max_length=200, null=False, unique=False)
    Interviewbit_username = models.CharField(
        max_length=200, null=False, unique=False)
    Atcoder_username = models.CharField(
        max_length=200, null=False, unique=False)
