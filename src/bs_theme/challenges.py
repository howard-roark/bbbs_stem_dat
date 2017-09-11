from .models import UserScore, Challenge
from django.contrib.auth.models import User
from pycipher import Caesar
import random

class Challenges():

	def caesar_i(self, rotate, plaintext, user_id):
		if (rotate and plaintext):
			# Get value of points for challenge
			# points_value = Challenge.objects.filter(id=1)
			# points_value = points_value.get_field('points_value')
			points_value = 1
			# Update UserScore table
			previous_score = UserScore.objects.get(user_id_id=user_id)
			previous_score.score += points_value
			previous_score.save()
			return Caesar(int(rotate)).encipher(str(plaintext), True)
		else:
			return ''

	def get_caesar(self, rotate, plaintext):
		if rotate and plaintext:
			return Caesar(int(rotate)).encipher(str(plaintext), True)
		else:
			return ''

	def caesar_ii(self, user_pt, user_rot, answer_pt, answer_rot, user_id):
		answer_correct = False
		if user_pt == answer_pt and user_rot == answer_rot:
			answer_correct = True
			points_value = 10
			# Update UserScore table
			previous_score = UserScore.objects.get(user_id_id=user_id)
			previous_score.score += points_value
			previous_score.save()

		return answer_correct

	# def get_caesar_ii(context):
	# 	context['C2_ROT_ACTUAL'] = random.randint(1,26)
	# 	context['C2_PT_ACTUAL'] = 'www.secret_stash.com'
	# 	context['C2_CT_ACTUAL'] = caesar(key=)
	# 	return caesar(key=context['rotate']).encipher(context['plaintext'])