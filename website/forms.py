from django.forms import ModelForm
from django.forms import ClearableFileInput
from .models import *

class ProductForm(ModelForm):
    class Meta:
            model = Product
            fields = '__all__'

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
        widgets = {'image': ClearableFileInput(attrs={'multiple': True})}


class VideoForm(ModelForm):
     class Meta:
          model = Video
          fields = '__all__'

class ShowreelForm(ModelForm):
     class Meta:
          model = Showreel
          fields = '__all__'


class MessageForm(ModelForm):
     class Meta:
          model = Message
          fields = '__all__'


class ReserveForm(ModelForm):
     class Meta:
          model = Reservation
          fields = '__all__'