from django import forms

class AnnouncementForm(forms.Form):
	username_attrs = {
		'placeholder': 'Username',
		'class': 'form-control',
	}

	title_attrs = {
		'placeholder': 'Title',
		'class': 'form-control',
	}

	content_attrs = {
		'placeholder': 'Write your post here...',
		'class': 'form-control',
		'rows': 5,
	}

	username = forms.CharField(label='', max_length = 20, widget = forms.TextInput(attrs = username_attrs))
	title = forms.CharField(label='', max_length = 50, widget = forms.TextInput(attrs = title_attrs))
	content = forms.CharField(label='', widget = forms.Textarea(attrs = content_attrs))