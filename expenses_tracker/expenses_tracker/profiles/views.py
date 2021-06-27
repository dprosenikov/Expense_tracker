from django.shortcuts import render, redirect

from expenses_tracker.expenses.models import ExpenseModel
from expenses_tracker.profiles.forms import ProfileForm
from expenses_tracker.profiles.models import ProfileModel


def profile_home(request):
    profile = ProfileModel.objects.first()
    name = profile.first_name + ' ' + profile.last_name
    expenses = ExpenseModel.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'name': name,
        'budget_left': budget_left
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    selected_profile = ProfileModel.objects.first()

    if request.method == 'POST':
        profile = ProfileForm(request.POST, instance=selected_profile)
        if profile.is_valid():
            profile.save()
            return redirect('profile')
        else:
            context = {'profile': profile}
            return render(request, 'profile-edit.html', context)
    else:
        profile = ProfileForm(instance=selected_profile)
        context = {
            'profile': profile
        }
        return render(request, 'profile-edit.html', context)


def delete_profile(request):
    selected_profile = ProfileModel.objects.first()
    expenses = ExpenseModel.objects.all()
    if request.method == 'POST':
        selected_profile.delete()
        expenses.delete()
        return redirect('home')
    else:
        return render(request, 'profile-delete.html')
