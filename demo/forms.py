from django.forms import ModelForm

from demo.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'