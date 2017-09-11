from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

class Challenge(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	points_value = models.PositiveSmallIntegerField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	points_limited = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

class UserScore(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
    	return '{\'user_id\': \'%s\', \'score\': %s}' % (self.user, self.score)

# class BsThemeAdmin(admin.ModelAdmin):
# 	pass