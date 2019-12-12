from django import forms

class TestimonyForm(forms.Form):
	username_attrs = {
		'placeholder': 'Username',
		'class': 'form-control',
		'readonly' : 'readonly',
	}

	title_attrs = {
		'placeholder': 'Title',
		'class': 'form-control',
	}

	content_attrs = {
		'placeholder': 'Write your testimony here...',
		'class': 'form-control',
		'rows': 5,
	}

	username = forms.CharField(label='', max_length = 20, widget = forms.TextInput(attrs = username_attrs))
	title = forms.CharField(label='', max_length = 50, widget = forms.TextInput(attrs = title_attrs))
	content = forms.CharField(label='', widget = forms.Textarea(attrs = content_attrs))