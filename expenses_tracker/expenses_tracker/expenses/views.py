from django.shortcuts import render, redirect

from expenses_tracker.expenses.forms import ExpensesForm, DeleteForm
from expenses_tracker.expenses.models import ExpenseModel
from expenses_tracker.profiles.forms import ProfileForm
from expenses_tracker.profiles.models import ProfileModel


def home(request):
    profile = ProfileModel.objects.first()
    if not profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ProfileForm()

        context = {'form': form}

        return render(request, 'home-no-profile.html', context)
    else:
        expenses = ExpenseModel.objects.all()
        budget_left = profile.budget - sum(e.price for e in expenses)
        context = {
            'expenses': expenses,
            'budget': profile.budget,
            'budget_left': budget_left
        }
        return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        expense = ExpensesForm(request.POST)
        if expense.is_valid():
            expense.save()
            return redirect('home')
        else:
            context = {'expense': expense}
            return render(request, 'expense-create.html', context)
    else:
        expense = ExpensesForm()
        context = {
            'expense': expense
        }
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    selected_expense = ExpenseModel.objects.get(pk=pk)
    if request.method == 'POST':
        expense = ExpensesForm(request.POST, instance=selected_expense)
        if expense.is_valid():
            expense.save()
            return redirect('home')
        else:
            context = {'expense': expense}
            return render(request, 'expense-edit.html', context)
    else:
        expense = ExpensesForm(instance=selected_expense)
        context = {
            'expense': expense,
            'selected_expense': selected_expense
        }
        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    selected_expense = ExpenseModel.objects.get(pk=pk)
    if request.method == 'POST':
        selected_expense.delete()
        return redirect('home')
    else:
        form = DeleteForm(instance=selected_expense)
        context = {'form': form}
        return render(request, 'expense-delete.html', context)
