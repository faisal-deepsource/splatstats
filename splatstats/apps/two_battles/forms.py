from django import forms
from .models import Rule, Match_Type, Ranks, Stage, Weapons


class FilterForm(forms.Form):
    rule = forms.ChoiceField(choices=Rule.choices)
    match_type = forms.ChoiceField(choices=Match_Type.choices)
    stage = forms.ChoiceField(choices=Stage)
    rank = forms.ChoiceField(choices=Ranks.choices)
    weapon = forms.ChoiceField(choices=Weapons)


class AdvancedFilterForm(forms.Form):
    query = forms.CharField()
