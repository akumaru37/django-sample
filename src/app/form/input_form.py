from django.forms import forms
from django.forms.fields import CharField

class InputForm(forms.Form):
    a = CharField(max_length=30, required=True, error_messages={
        'required': 'Aを入力してください',
    })

    def __init__(self, *arags, **kwargs):
        super().__init__(*arags, **kwargs)
        # self.fields["a"] = CharField(max_length=30, required=True, error_messages={
        #     'required': 'Aを入力してください',
        # })
        for i in range(0, 7):
            self.fields["d[" + str(i) + "]"] = CharField(
                required=True,
                error_messages={
                    'required': "d" + str(i) + "を入力してください"
                }
            )
