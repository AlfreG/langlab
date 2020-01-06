from django import forms
'''
https://docs.djangoproject.com/en/3.0/ref/forms/fields/

required: To specify that a field is not required, pass required=False to the Field constructor:
label: lets you specify the “human-friendly” label for this field. This is used when the Field is displayed in a Form.

'''

class ContactForm(forms.Form):

    sender = forms.EmailField(min_length=5, max_length=20, label="email", required=True)
    message = forms.CharField(min_length=10, max_length=250, strip=True, label="message", required=False)
