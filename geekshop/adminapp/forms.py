from django import forms
from mainapp.models import Product, ProductCategory


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.item():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProductCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.item():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''