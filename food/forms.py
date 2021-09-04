from django import forms

COFFEE_CHOICES = [
    ('Cold Coffee', 'Cold Coffee'),
    ('Hot Coffee', 'Hot Coffee'),
    ('AFFOGATO','AFFOGATO'),
    ('AMERICANO ','AMERICANO'),
    ('CAPPUCCINO','CAPPUCCINO'),
    ('COLD BREW COFFEE','COLD BREW COFFEE'),
    ('ICED MOCHA','ICED MOCHA'),
    ('IRISH COFFEE','IRISH COFFEE'),

]

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    coffee_order = forms.ChoiceField(choices=COFFEE_CHOICES, widget=forms.Select())