from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UDevice(models.Model):
	UID = models.CharField(max_length = 100, primary_key = True)
	UserName = models.CharField(max_length = 100, default='UserName not mapped')

class Log(models.Model):
	UserDevice = models.CharField(max_length = 100, blank = False)
	EventName = models.CharField(max_length = 100, blank = False)
	EventLabel = models.CharField(max_length = 100, blank = False)
	EventAction = models.CharField(max_length = 100, blank = False)
	EventTime = models.DateTimeField(auto_now_add = True)

class BlockedEvents(models.Model):
	EventName = models.CharField(max_length = 100, blank = False, default = '', primary_key = True)
	Counter = models.IntegerField(default = 0)