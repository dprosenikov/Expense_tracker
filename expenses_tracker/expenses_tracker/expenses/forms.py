from django import forms

from expenses_tracker.expenses.models import ExpenseModel


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = '__all__'


class DeleteForm(ExpensesForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'