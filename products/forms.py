from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))
    description = forms.CharField(
                        required=True, 
                        widget=forms.Textarea(
                                attrs={
                                    'placeholder': 'Your Description',
                                    'class': 'new-class-name two',
                                    'id':'my-id-for-textarea'}))
    price = forms.DecimalField(initial=199.99)
    # above overrides below
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get(title)
class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))
    description = forms.CharField(required=True, widget=forms.Textarea(
                                                            attrs={
                                                                'placeholder': 'Your Description',
                                                                'class': 'new-class-name two',
                                                                'id':'my-id-for-textarea'}))
    price = forms.DecimalField(initial=199.99)