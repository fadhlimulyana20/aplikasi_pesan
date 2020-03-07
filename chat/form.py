from django import forms
from .models import Chat

class Create_chat(forms.ModelForm):
    class Meta:
        model = Chat
        exclude = ['sender']
        # widgets = {
        #     'birth_date': DateInput()
        # }
        
    def __init__(self, *args, **kwargs):
        super(Create_chat, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['placeholder'] = 'Pesan Anda'
        self.fields['destination'].widget.attrs['placeholder'] = 'Kepada'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.field.help_text :
                 visible.field.widget.attrs.update({'class':'form-control has-popover', 'data-content':visible.field.help_text, 'data-placement':'bottom', 'data-container':'body'})