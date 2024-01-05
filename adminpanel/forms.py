# myapp/forms.py
from django import forms
from .models import CustomUser
from .models import CustomerRepository
from .models import Frequest_query_set

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']


# forms.py

class UploadCsvForm(forms.Form):
    file = forms.FileField()


class QueryForm(forms.Form):
    complain_id = forms.CharField(label='Complain ID', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_id = forms.CharField(label='Customer ID', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    complained_through = forms.CharField(label='Complained through', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_no= forms.CharField(label='Mobile No', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    account_number = forms.CharField(label='Account Number', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Frequest_query_set.objects.values_list('category', flat=True).distinct(),widget=forms.Select(attrs={'class': 'form-control'}))
    query = forms.ChoiceField(choices=[],widget=forms.Select(attrs={'class': 'form-control'}))  # Empty choices for initial rendering
    other_query = forms.CharField(label='Other Queries', max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    remarks = forms.CharField(label='Remarks', max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        # Set initial choices for the query dropdown based on the selected category
        category = self.fields['category'].widget.attrs.get('value', None)
        if category:
            self.fields['query'].choices = Frequest_query_set.objects.filter(category=category).values_list('query', 'query')
            
    
    