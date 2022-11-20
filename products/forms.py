from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from .models import AllProducts, CategoryGroupings, SubCategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = AllProducts
        fields = '__all__'

        widgets = {
            'description': SummernoteWidget(),
            'image': CustomClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # taken from boutique ado walkthrough to display friendly names
        categories = CategoryGroupings.objects.all()
        sub_categories = SubCategory.objects.all()
        category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in categories]
        sub_category_friendly_names = [
            (c.id, c.get_friendly_name()) for c in sub_categories]

        self.fields['category'].choices = category_friendly_names
        self.fields['sub_category'].choices = sub_category_friendly_names
        self.fields['current_rating'].widget.attrs['readonly'] = True
        self.fields['accumulative_rating'].widget.attrs['readonly'] = True
        self.fields['number_of_ratings'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
        self.fields['slug'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['sku'].widget.attrs['readonly'] = True

        placeholders = {}
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{field} *'
            else:
                placeholder = field
            if field == 'image':
                self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'aria-label'] = placeholder
