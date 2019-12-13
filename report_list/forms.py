from django import forms

class ReportForm(forms.Form):
    form_title_attrs = {
        'placeholder' : 'Title',
        'class' : 'form-control',
    }
    location_attrs = {
        'placeholder' : 'Location',
        'class' : 'form-control',
    }
    time_attrs = {
        'placeholder' : 'Time',
        'class' : 'form-control',
    }
    category_attrs = {
        'placeholder' : 'Category',
        'class' : 'form-control',
    }
    description_attrs = {
        'placeholder' : 'Write your description here...',
        'class' : 'form-control',
    }

    form_title = forms.CharField(label= '', max_length = 50, widget = forms.TextInput(attrs = form_title_attrs))
    location = forms.CharField(label= '', max_length = 50, widget = forms.TextInput(attrs = location_attrs))
    time = forms.TimeField(label= '', widget = forms.TimeInput(attrs = time_attrs))
    category = forms.CharField(label= '', max_length = 50, widget = forms.TextInput(attrs = category_attrs))
    description = forms.CharField(label = '', widget = forms.Textarea(attrs = description_attrs))