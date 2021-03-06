from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import RegisterForm

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("profile"))
	else:
		form = RegisterForm()
	return render(response, "registration/register.html", {"form":form})



