from django import forms
from .models import specials, cleared_failed, fail_reasons, stages


class FilterForm(forms.Form):
    special = forms.ChoiceField(choices=specials)
    stage = forms.ChoiceField(choices=stages)
    cleared = forms.ChoiceField(choices=cleared_failed)
    failreason = forms.ChoiceField(choices=fail_reasons)


class AdvancedFilterForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea(attrs={"rows": 20, "cols": 40}))
