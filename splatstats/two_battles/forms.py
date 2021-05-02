from django import forms
from .models import Rule, Match_Type, Ranks, Stage, Weapons


class BattleForm(forms.Form):
    splatnet_json = forms.JSONField(required=False)
    stat_ink_json = forms.JSONField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        splatnet_json = cleaned_data.get("splatnet_json")
        stat_ink_json = cleaned_data.get("stat_ink_json")

        if splatnet_json is None and stat_ink_json is None:
            msg = "Must enter at least one form of data."
            self.add_error("splatnet_json", msg)
            self.add_error("stat_ink_json", msg)


class FilterForm(forms.Form):
    rule = forms.ChoiceField(choices=Rule.choices)
    match_type = forms.ChoiceField(choices=Match_Type.choices)
    stage = forms.ChoiceField(choices=Stage)
    rank = forms.ChoiceField(choices=Ranks.choices)
    weapon = forms.ChoiceField(choices=Weapons)


class AdvancedFilterForm(forms.Form):
    query = forms.CharField()
