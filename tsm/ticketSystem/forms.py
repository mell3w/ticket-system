from django import forms
from .models import Applications

class ApplicationsForm(forms.Form):
    model = Applications
    exclude = ['counted_eq']


#-------------------------------------------------------------------------------------------------------
#               Создадим форму для редактирования модели
#-------------------------------------------------------------------------------------------------------

class ChangeAppForm(forms.Form):
    class Meta:
        model = Applications
        fields = ('treaty','ykp7','ykp12','rf','tm','md','door_closer',
                  'img_door_closer','monetary', 'price', 'premium','change')
