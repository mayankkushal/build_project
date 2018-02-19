# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

import requests

from .models import *
from .forms import BasicForm, LoginForm

# Create your views here.

# class BasicView(FormView):
# 	form_class = BasicForm
# 	template_name = "initial/form.html"
# 	success_url = "/"

# 	def form_valid(self, form):
# 		print(self.request.GET)
# 		return super(BasicView, self).form_valid(form)

# 	def get_context_data(self, **kwargs):
# 		context = super(BasicView, self).get_context_data(**kwargs)
# 		# context['push'] = BasicModel.objects.all()
# 		return context


def form(request):
	if request.method == 'POST':
		for p, k in request.POST.items():
			print(p, k)

		post = request.POST

		internal = post.getlist('internal')
		stand_push = post.getlist('stand_push')
		external = post.getlist('external')

		cl = Codeline.objects.create(
				codeline_name=post.get('c_name'),
				parent_codeline=post.get('p_name'),
				bug_id=post.get('bug'),
				tag=post.get('tag'),
				build_setup="test",
				username="test"
			)
		if internal:
			for i in internal:
				BuildList.objects.create(
						codeline=cl,
						build_name=i,
						isinternal=True
					)
		if stand_push:
			for i in stand_push:
				BuildList.objects.create(
						codeline=cl,
						build_name=i,
						standard_push=True
					)
		if external:
			for i in external:
				BuildList.objects.create(
						codeline=cl,
						build_name=i,
					)

		
		return render(request, "initial/form.html")

	if request.method == "GET":
		return render(request, "initial/form.html")


def ldap_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponse("Disabled account")
                    # Return a 'disabled account' error message
            else:
                # Return an 'invalid login' error message.
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request,"initial/login.html",{'form':form})