from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

app_name = 'bs_theme'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^challenges/$', views.challenge_list, name='challenges'),
    url(r'^caesar_i/$', views.caesar_i, name='caesar_i'),
    url(r'^caesar_i/(?P<rotate>\d+)', views.caesar_i, name='caesar_i'),
    url(r'^caesar_ii/$', views.caesar_ii, name='caesar_ii'),
    url(r'^caesar_ii/(?P<rotate>\d+)', views.caesar_ii, name='caesar_ii'),
    url(r'^register/$', CreateView.as_view(
            template_name='registration_form.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url(r'^accounts/register/$', views.register, name='register'),
]
