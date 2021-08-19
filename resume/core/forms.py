from django.forms import ModelForm
from .models import Contact
# Create your forms here.

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'