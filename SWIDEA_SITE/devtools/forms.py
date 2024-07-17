from devtools.models import Devtools
from django import forms


class DevtoolsForm(forms.ModelForm):
    class Meta():
        model = Devtools
        fields = ('__all__')