from django import forms


class BattleForm(forms.Form):
    splatnet_json = forms.JSONField(required=False)
    stat_ink_json = forms.JSONField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        splatnet_json = cleaned_data.get("splatnet_json")
        stat_ink_json = cleaned_data.get("stat_ink_json")

        if splatnet_json == None and stat_ink_json == None:
            msg = "Must enter at least one form of data."
            self.add_error("splatnet_json", msg)
            self.add_error("stat_ink_json", msg)
