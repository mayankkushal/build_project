# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView

import requests

from .models import *
from .forms import BasicForm

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

		url = 'https://jsonplaceholder.typicode.com/users'
		r = requests.get(url)
		data = r.json()
		post = request.POST

		cl = Codeline.objects.create(
				codeline_name=post.get('c_name'),
				parent_codeline=post.get('p_name'),
				bug_id=post.get('bug'),
				tag=post.get('tag'),
				build_setup="test",
				username="test"
			)

		for d in data:
			if request.POST.get(d['name']):
				bl = BuildList.objects.create(
						codeline=cl,
						build_name=d['name']
					)
		return render(request, "initial/form.html")

	if request.method == "GET":
		return render(request, "initial/form.html")