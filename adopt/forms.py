from django import forms
from django.db.models import Max

from .models import User, Pet, Comment, Organization



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field.widget, forms.CheckboxInput):
                visible.field.widget.attrs["class"] = "form-control-input floating"
            else:
                visible.field.widget.attrs["class"] = "form-control floating"
            visible.field.widget.attrs["id"] = visible.name
            visible.field.label = visible.label
            visible.field.label_suffix = ''
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs["rows"] = 1


# Form for inserting (CREATE)
class PetCreateForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = [
            'name', 'type', 'breed', 'gender', 'age', 'size', 'description', 
            'adopted_by', 'fostered_by',
            'energy', 'anxiety', 
            'sterilized', 'vaccinated',
            'dog_friendly', 'kid_friendly', 'cat_friendly',
            'house_trained', 'leash_trained', 'crate_trained',
            'images'
            ]
        widgets = {
            'registered_date': forms.HiddenInput(),
            'registered_by': forms.HiddenInput(),        
        }


    def __init__(self, *args, **kwargs):
        super(PetCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control floating"
            visible.field.widget.attrs["id"] = visible.name
            visible.field.label = visible.label
            visible.field.label_suffix = ''
            if isinstance(visible.field.widget, forms.Textarea):
                 visible.field.widget.attrs["rows"] = 5
        

class PetSearchForm(forms.Form):

    # Remove the UNKNOWN option from all the visible fields when search
    CHOICES = [(key, value) for key, value in Pet.CHOICES if key != 'UNKNOWN']
    LEVELS = [(key, value) for key, value in Pet.LEVELS if key != 'UNKNOWN']
    PROGRESS = [(key, value) for key, value in Pet.PROGRESS if key != 'UNKNOWN']

    # Define the necessary fields for the search criteria
    type = forms.MultipleChoiceField(choices=Pet.ANIMALS, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    age = forms.MultipleChoiceField(choices=Pet.AGES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    size = forms.MultipleChoiceField(choices=Pet.SIZES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    gender = forms.MultipleChoiceField(choices=Pet.GENDER, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    
    sterilized = forms.MultipleChoiceField(choices=CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    vaccinated = forms.MultipleChoiceField(choices=CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))

    dog_friendly = forms.MultipleChoiceField(choices=CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    kid_friendly = forms.MultipleChoiceField(choices=CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    cat_friendly = forms.MultipleChoiceField(choices=CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))

    house_trained = forms.MultipleChoiceField(choices=PROGRESS, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    leash_trained = forms.MultipleChoiceField(choices=PROGRESS, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    crate_trained = forms.MultipleChoiceField(choices=PROGRESS, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))

    energy = forms.MultipleChoiceField(choices=LEVELS, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))
    anxiety = forms.MultipleChoiceField(choices=LEVELS, required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control floating'}))


    def __init__(self, *args, **kwargs):
        super(PetSearchForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control-input"
            visible.field.widget.attrs["id"] = visible.name
            visible.field.label = visible.label
            visible.field.label_suffix = ''
    
    # Ensure at least one search parameter is provided
    def clean(self):
        cleaned_data = super().clean()

        # Remove errors for optional fields
        for field in self.fields:
            if field in self.errors:
                del self.errors[field]
    
        return cleaned_data
