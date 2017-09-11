from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic.edit import FormView 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserScore, Challenge
from django.db.models import Count
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .challenges import Challenges
import random

def index(request):
    top_users = UserScore.objects.order_by('-score')[:5]
    context = {'top_users': top_users}
    return render(request, 'bs_theme/index.html', context)

def challenge_list(request):
    items = Challenge.objects.order_by('id')
    context = {'problems': items}
    return render(request, 'bs_theme/challenge_list.html')

def caesar_i(request, rotate='', plaintext=''):
    challenge = Challenge.objects.filter(id=1)
    choices = []
    for x in range(1,27):
        choices.append(x)
    context = {'challenge':challenge, 'choices': choices}

    if request.method == 'GET':
        data = request.GET
        plaintext = data.get('pt')
        rotate = str(data.get('rot'))
        user_id = data.get('user_id')
        c = Challenges()
        ct = c.caesar_i(rotate, plaintext, user_id)
        context.update({'pt':plaintext, 'rot':rotate, 'ct':ct})
    return render(request, 'bs_theme/caesar_i.html', context)

def caesar_ii(request):
    c = Challenges()
    challenge = Challenge.objects.filter(id=2)
    choices = []
    for x in range(1,27):
        choices.append(x)

    answer_pt = 'www.secretstash.com'

    if request.method == 'GET':
        data = request.GET
        user_pt = data.get('user_pt')
        user_rot = str(data.get('user_rot'))
        answer_rot = data.get('answer_rot')
        answered = data.get('answered')
        print answered
        print 'pre answer_rot: ' + str(answer_rot)
        if not answer_rot or answered:
            answer_rot = random.randint(1,26)
        print answer_rot
        answer_ct = c.get_caesar(answer_rot, answer_pt)
        context = {'challenge':challenge,
            'choices': choices,
            'answer_ct':answer_ct,
            'answer_rot': answer_rot}

        user_id = data.get('user_id')
        c = Challenges()
        correct = c.caesar_ii(user_pt, user_rot, answer_pt, answer_rot, user_id)
        if correct:
            context.update({'correct':correct})

    return render(request, 'bs_theme/caesar_ii.html', context)

def login(request):
	return render(request, 'bs_theme/login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/registration_form.html', {'form':form})

def registration_complete(request):
    return render (request, '../../index.html')

@receiver(post_save, sender=User)
def init_new_user(sender, **kwargs):
    user = kwargs.get('instance')
    user_score = UserScore(user_id=user, score=0)
    try:
        user_score.save()
    except:
        pass
