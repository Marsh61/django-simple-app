from django import forms
from .models import Product 

class ProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "class-one class-two",
                "rows": 20,
                "cols": 20
            }
        )
    )
    price = forms.DecimalField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("not a valid title")
        else:
            return title

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "class-one class-two",
                "rows": 20,
                "cols": 20
            }
        )
    )
    price = forms.DecimalField()