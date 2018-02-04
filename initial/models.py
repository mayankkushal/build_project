# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Codeline(models.Model):
	"""
	Basic model to be used in the form
	"""
	codeline_name = models.CharField('Name', max_length=50)
	parent_codeline = models.CharField('Parent', max_length=50)
	tag = models.CharField('Tag', max_length=50)
	bug_id = models.CharField("Bug Id", max_length=50)
	do_push = models.BooleanField()
	build_setup = models.CharField("Wrapper Build Setup", max_length=50)
	sanity_setup = models.BooleanField()
	username = models.CharField("Username", max_length=50)

	def __str__(self):
		return self.username

class BuildList(models.Model):
	codeline = models.ForeignKey('codeline', on_delete=models.CASCADE)
	build_name = models.CharField("Build Name", max_length=50)
	isinternal = models.BooleanField()
	standard_push = models.BooleanField()

	def __str__(self):
		return self.build_name
