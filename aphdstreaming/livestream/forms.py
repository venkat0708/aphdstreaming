from django import forms

from crispy_forms.helper import FormHelper

from .models import  Event
from .widgets import XDSoftDateTimePickerInput


class DateInput(forms.DateInput):
	input_type = 'date'

class EventForm(forms.ModelForm):
	"""form for Event"""
	time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())
	start_date_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())
	end_date_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())

	helper = FormHelper()
	helper.form_tag = False
	helper.form_style = 'inline'

	class Meta:
		model = Event
		exclude = ['']
