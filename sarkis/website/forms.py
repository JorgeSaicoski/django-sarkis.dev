from django import forms

from website.models import Message


# create a ModelForm


class ContactForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "title": forms.TextInput(attrs={"placeholder": "Title"}),
            "description": forms.Textarea(attrs={"placeholder": "Message"}),
        }
