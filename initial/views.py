# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView

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
		return render(request, "initial/form.html")

	if request.method == "GET":
		return render(request, "initial/form.html")