
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(category.id, category.cat_name) for category in categories]
        self.fields['category'].choices = category_choices        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'my-1'

