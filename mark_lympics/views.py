from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .forms import UserRegistrationForm


def index(request):
    return render(request, 'mark_lympics/index.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = UserRegistrationForm()
    return render(request, 'mark_lympics/register.html', args)
