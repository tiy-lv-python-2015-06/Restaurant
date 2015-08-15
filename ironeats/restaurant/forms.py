from django.forms import ModelForm
from restaurant.models import FoodItem


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ('name', 'price', 'description', 'category', )